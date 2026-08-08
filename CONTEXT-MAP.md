# AgentCFO context map

本仓库采用多 Context。Agent 先读根 [`CONTEXT.md`](CONTEXT.md)，再按任务域加载下表文件。

| 任务域 | Context | 主要路径 | 约束 |
| --- | --- | --- | --- |
| 产品与 PM | [`docs/contexts/product.md`](docs/contexts/product.md) | `docs/pm/`、`docs/outputs/` | PRD 批准前不写业务代码 |
| 前端 | [`docs/contexts/frontend.md`](docs/contexts/frontend.md) | `frontend/` | 同时遵守 `frontend/CLAUDE.md` |
| 后端与 CAW | [`docs/contexts/backend.md`](docs/contexts/backend.md) | `app/`、`tests/`、`docs/backend/` | 风控和审批不得下放给 LLM；契约以代码+测试为准 |
| 资产与交付 | [`docs/contexts/assets.md`](docs/contexts/assets.md) | `inbox/`、`assets/` | 新资产先投递再归档；路径见 `assets/ASSET-MAP.md` |

## 跨域工作

跨两个以上产品层根时，先在 `docs/outputs/handoff/<theme>/` 写任务 handoff（覆盖式更新；不要假设存在 `docs/agents/handoff.md`），列明：

- 变更目录；
- 契约影响；
- 验证方式；
- 负责人和 Review Gate。

首个 theme：`treasury-payout`。
