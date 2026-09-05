import os
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Mapping, Protocol, runtime_checkable

from pydantic import BaseModel


class MissingCawReadOnlyConfig(RuntimeError):
    pass


class CawPactStatus(BaseModel):
    pactId: str
    providerStatus: str


class CawTransactionRecord(BaseModel):
    requestId: str
    providerStatus: str
    txHash: str | None = None
    error: str | None = None


class CawWalletAddress(BaseModel):
    address: str
    chainId: str | None = None


@runtime_checkable
class CawReadOnlyClient(Protocol):
    def get_pact_status(self, pact_id: str) -> CawPactStatus:
        ...

    def get_transaction_by_request_id(self, request_id: str) -> CawTransactionRecord:
        ...

    def list_transactions(self, filters: Mapping[str, str]) -> list[CawTransactionRecord]:
        ...

    def list_audit_logs(self, filters: Mapping[str, str]) -> list[dict[str, Any]]:
        ...

    def list_wallet_addresses(self) -> list[CawWalletAddress]:
        ...


class FakeCawReadOnlyClient(CawReadOnlyClient):
    def __init__(
        self,
        pact_statuses: Mapping[str, str] | None = None,
        transactions: Mapping[str, CawTransactionRecord] | None = None,
        audit_logs: list[dict[str, Any]] | None = None,
        wallet_addresses: list[CawWalletAddress] | None = None,
    ):
        self.pact_statuses = dict(pact_statuses or {})
        self.transactions = dict(transactions or {})
        self.audit_logs = list(audit_logs or [])
        self.wallet_addresses = list(wallet_addresses or [])

    def get_pact_status(self, pact_id: str) -> CawPactStatus:
        return CawPactStatus(
            pactId=pact_id,
            providerStatus=self.pact_statuses[pact_id],
        )

    def get_transaction_by_request_id(self, request_id: str) -> CawTransactionRecord:
        return self.transactions[request_id]

    def list_transactions(self, filters: Mapping[str, str]) -> list[CawTransactionRecord]:
        if not filters:
            return list(self.transactions.values())
        return [
            transaction
            for transaction in self.transactions.values()
            if all(getattr(transaction, key) == value for key, value in filters.items())
        ]

    def list_audit_logs(self, filters: Mapping[str, str]) -> list[dict[str, Any]]:
        if not filters:
            return self.audit_logs
        return [
            audit_log
            for audit_log in self.audit_logs
            if all(audit_log.get(key) == value for key, value in filters.items())
        ]

    def list_wallet_addresses(self) -> list[CawWalletAddress]:
        return self.wallet_addresses


@dataclass(frozen=True)
class CawReadOnlyConfig:
    mode: str = "fake"
    api_url: str | None = None
    api_key: str | None = None
    wallet_id: str | None = None

    @classmethod
    def from_mapping(cls, config: Mapping[str, str] | None = None):
        source = config or os.environ
        mode = _optional_value(source, "CAW_READ_ONLY_MODE")
        if mode is None:
            mode = _optional_value(source, "CAW_ADAPTER_MODE") or "fake"
        return cls(
            mode=mode.strip().lower(),
            api_url=_optional_value(source, "AGENT_WALLET_API_URL"),
            api_key=_optional_value(source, "AGENT_WALLET_API_KEY"),
            wallet_id=_optional_value(source, "AGENT_WALLET_WALLET_ID"),
        )

    def validate_real(self):
        if self.mode != "real":
            return
        if not self.api_url or not self.api_key or not self.wallet_id:
            raise MissingCawReadOnlyConfig(
                "CAW read-only real mode is not configured. "
                "AGENT_WALLET_API_URL, AGENT_WALLET_API_KEY, and "
                "AGENT_WALLET_WALLET_ID are required."
            )


class RealCawReadOnlyClient(CawReadOnlyClient):
    def __init__(
        self,
        config: CawReadOnlyConfig,
        sdk_client: Any | None = None,
        sdk_client_factory: Callable[[str, str], Any] | None = None,
    ):
        config.validate_real()
        self.config = config
        self._sdk_client = sdk_client
        self._sdk_client_factory = sdk_client_factory

    def get_pact_status(self, pact_id: str) -> CawPactStatus:
        pact = self._client().get_pact(pact_id)
        return CawPactStatus(
            pactId=pact_id,
            providerStatus=str(_result_value(pact, "status")),
        )

    def get_transaction_by_request_id(self, request_id: str) -> CawTransactionRecord:
        transaction = self._client().get_user_transaction_by_request_id(
            self.config.wallet_id,
            request_id,
            ext=True,
        )
        return _transaction_record_from_provider(transaction, request_id)

    def list_transactions(self, filters: Mapping[str, str]) -> list[CawTransactionRecord]:
        transactions = self._client().list_user_transactions(
            wallet_uuid=self.config.wallet_id,
            status=filters.get("status"),
            token_id=filters.get("tokenId"),
            chain_id=filters.get("chainId"),
            ext=True,
        )
        return [
            _transaction_record_from_provider(transaction, _request_id_fallback(transaction))
            for transaction in _result_items(transactions)
        ]

    def list_audit_logs(self, filters: Mapping[str, str]) -> list[dict[str, Any]]:
        audit_logs = self._client().list_audit_logs(
            wallet_id=self.config.wallet_id,
            action=filters.get("action"),
            result=filters.get("result"),
            limit=_int_or_none(filters.get("limit")),
        )
        return [_redact_audit_log(log) for log in _result_items(audit_logs)]

    def list_wallet_addresses(self) -> list[CawWalletAddress]:
        addresses = self._client().list_wallet_addresses(self.config.wallet_id)
        return [
            CawWalletAddress(
                address=str(_result_value(address, "address")),
                chainId=_string_or_none(_result_value(address, "chain_id")),
            )
            for address in _result_items(addresses)
            if _result_value(address, "address")
        ]

    def _client(self):
        if self._sdk_client is not None:
            return self._sdk_client
        if self._sdk_client_factory is not None:
            return self._sdk_client_factory(self.config.api_url, self.config.api_key)

        from cobo_agentic_wallet.client import WalletAPIClient

        return WalletAPIClient(
            base_url=self.config.api_url,
            api_key=self.config.api_key,
        )


def create_caw_read_only_client(
    config: Mapping[str, str] | None = None,
) -> CawReadOnlyClient:
    read_only_config = CawReadOnlyConfig.from_mapping(config)
    if read_only_config.mode in {"fake", "mock"}:
        return FakeCawReadOnlyClient()
    if read_only_config.mode == "real":
        return RealCawReadOnlyClient(read_only_config)
    raise MissingCawReadOnlyConfig("Unsupported CAW read-only mode")


def _optional_value(source: Mapping[str, str], key: str) -> str | None:
    value = source.get(key)
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None


def _result_value(result, key: str):
    if isinstance(result, Mapping):
        return result.get(key)
    return getattr(result, key, None)


def _result_items(result) -> list:
    if result is None:
        return []
    if isinstance(result, list):
        return result
    for key in ("items", "data", "results", "transactions", "logs", "addresses"):
        value = _result_value(result, key)
        if isinstance(value, list):
            return value
    return []


def _request_id_fallback(transaction) -> str:
    value = _result_value(transaction, "request_id") or _result_value(transaction, "requestId")
    return str(value) if value is not None else ""


def _transaction_record_from_provider(transaction, fallback_request_id: str) -> CawTransactionRecord:
    request_id = (
        _result_value(transaction, "request_id")
        or _result_value(transaction, "requestId")
        or fallback_request_id
    )
    status = (
        _result_value(transaction, "status")
        or _result_value(transaction, "status_code")
        or _result_value(transaction, "providerStatus")
    )
    tx_hash = _result_value(transaction, "transaction_hash") or _result_value(transaction, "tx_hash")
    error = "provider_failed" if _provider_has_error(transaction) else None
    return CawTransactionRecord(
        requestId=str(request_id),
        providerStatus=str(status),
        txHash=_string_or_none(tx_hash),
        error=error,
    )


def _provider_has_error(transaction) -> bool:
    return any(
        _result_value(transaction, key)
        for key in ("error", "failed_reason", "failure_reason", "reject_reason")
    )


def _redact_audit_log(audit_log) -> dict[str, Any]:
    source = dict(audit_log) if isinstance(audit_log, Mapping) else dict(vars(audit_log))
    return {key: _redact_value(key, value) for key, value in source.items()}


def _redact_value(key: str, value):
    lowered = key.lower()
    if any(marker in lowered for marker in ("api_key", "authorization", "private_key", "secret", "credential")):
        return "[redacted]"
    if isinstance(value, Mapping):
        return {inner_key: _redact_value(inner_key, inner_value) for inner_key, inner_value in value.items()}
    if isinstance(value, list):
        return [_redact_value(key, item) for item in value]
    return value


def _int_or_none(value: str | None) -> int | None:
    return int(value) if value else None


def _string_or_none(value) -> str | None:
    return str(value) if value is not None else None
