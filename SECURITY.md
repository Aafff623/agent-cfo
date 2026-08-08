# Security

## Do not commit secrets

Never commit API keys, wallet private keys, `.env` files, cookies, or unredacted credentials. Demo defaults to **mock mode** and must not require real CAW secrets.

Put secrets only in local / host env (e.g. Render), never in the repo or frontend `NEXT_PUBLIC_*` for provider keys.

## Reporting a vulnerability

Prefer **[GitHub Private Vulnerability Reporting](https://github.com/Aafff623/agent-cfo/security/advisories/new)** (Security → Advisories).

If private reporting is unavailable, open an Issue titled `[security]` with **no secrets** in the body; maintainers will follow up privately.

## Scope notes

- Mock / demo paths are not production custody.
- Do not treat mock tx hashes as on-chain proof.
