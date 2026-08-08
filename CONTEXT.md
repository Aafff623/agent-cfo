# AgentCFO context

AgentCFO 是面向 Web3 小团队和 DAO 的受控财务 Agent。核心流程：

```text
Contribution Records → Payment Plan → Risk Check → Human Approval
→ Cobo Agentic Wallet → Audit Report
```

## 当前目标

项目从黑客松 Demo 继续演进为 production-ready 产品。现阶段优先保证：

1. mock、testnet、real 能力边界真实可辨；
2. 风控与人工审批始终位于资金执行之前；
3. 前后端契约以 `app/models.py`、`app/routers/payments.py`、`tests/test_mvp_flow.py` 为准（代码 + 测试是唯一 runtime 真相）；
4. 新业务工作采用 `docs/outputs/report → prd → handoff`（复数 `outputs`）；
5. 竞赛期物理资产路径（如 `assets/theme/ppt/`）见 `assets/ASSET-MAP.md`；**canonical 以最新 project-init 为准**（`assets/ppt/` · `assets/speeches/`），不做假装迁移。

## 产品层根

- 前端：`frontend/`
- 后端：`app/`
- 后端测试：`tests/`
- 产品与交付文档：`docs/`
- 交付资产：`assets/`
- 待归类投递：`inbox/`

## 首个业务 theme

`treasury-payout`

该 theme 在 Project Init Gate 通过后进入 PRD 阶段。Gate 前不大规模业务编码（允许治理、目录、索引与 README Polish 工具链）。

## Context 路由

多 Context 入口见 [`CONTEXT-MAP.md`](CONTEXT-MAP.md)，详细领域文件位于 `docs/contexts/`。

## 单一事实源

| 事实类型 | 唯一入口 |
| --- | --- |
| 领域术语与硬约束 | 本文件 + `docs/contexts/*` |
| 共享用词 | 根 [`LANGUAGES.md`](LANGUAGES.md) |
| Agent 硬约束 / 任务流门禁 | 根 [`AGENTS.md`](AGENTS.md) |
| 人读摘要与运行说明 | 根 [`README.md`](README.md) |

禁止再维护 `docs/agents/language.md` / `docs/agents/context.md`。
