# Domain map

> Matt `setup-matt-pocock-skills` / `domain-modeling` 消费本文件。领域术语细节在根 `CONTEXT.md` 与 `docs/contexts/*`。

## 布局

- **多 Context**：根 `CONTEXT-MAP.md` → `docs/contexts/{product,frontend,backend,assets}.md`
- **系统级 ADR**：`docs/adr/`
- 读领域词先 CONTEXT，再改代码；变更术语时用 `domain-modeling` 写回 CONTEXT / ADR

## 核心领域

| 领域 | 责任 | 代码 / 文档 |
| --- | --- | --- |
| Contribution | 贡献记录与订阅账单输入 | `frontend/lib/demo/`、API models |
| Planning | 付款计划与解释 | `app/services/payment_planner.py` |
| Risk | 确定性预算、白名单、限额、token、重复检查 | `app/services/risk_engine.py` |
| Approval | 人工确认与可执行项选择 | `app/routers/payments.py`、Console |
| Execution | CAW mock / testnet 执行 | `app/services/caw_adapter.py` |
| Observation | CAW 状态只读刷新 | `app/services/caw_observer.py` |
| Audit | 决策与执行证据快照 | `AuditReport`、SQLite store |
| Agent Chat | Treasury 解释与操作引导 | MiniMax 后端代理 |

## 授权边界

LLM 不得决定 Risk、Approval 或 CAW policy。生产环境中的 `approvedBy` 必须来自可信身份，不得继续信任任意客户端字符串。

## 事实层级

1. 运行时代码和测试（最高）；
2. 根 `CONTEXT.md` / `LANGUAGES.md` / `AGENTS.md`；
3. `README.md` 与 `docs/backend/`（人读；不得推翻代码）；
4. `docs/outputs/` 中已批准的 PRD 与 handoff；
5. `docs/pm/` 历史任务记录；
6. PPT、视频和营销文案。

下层来源不得推翻上层事实。
