# AgentCFO — 真实事实

AgentCFO 是面向 Web3 小团队 / DAO 的受控财务 Agent。核心流程：
`Contribution Records → Payment Plan → Risk Check → Human Approval → Cobo Agentic Wallet → Audit Report`。默认 mock demo，真金路径 opt-in 且 fail-closed。

## 关键事实

- 技术栈：后端 Python 3 + FastAPI + Pydantic（`app/`，测试 `tests/`，依赖 `requirements.txt`）；前端 Next.js + TypeScript（`frontend/`，包管理 pnpm）。
- API（P0 端点）：`POST /api/payment-plan`、`POST /api/risk-check`、`POST /api/execute-payment`、`GET /api/audit-report/{id}`、`GET /api/caw-status/{id}`、`POST /api/agent/chat`。契约真相：`app/models.py` + `app/routers/payments.py` + `tests/test_mvp_flow.py`。
- LLM：Agent Hub 聊天经后端代理 MiniMax OpenAI 兼容 API，key 仅在后端 env `MINIMAX_API_KEY`；Payment Plan 可选 OpenAI planner（`PAYMENT_PLANNER_MODE=openai`）。文档默认中文，API 字段 / 命令保留英文。
- 部署：前端 Vercel（agentcfo-frontend.vercel.app），后端 Render（agentcfo-backend.onrender.com），均默认 mock。
- Demo 数据（全团队对齐）：Alice 20 / Bob 15（blocked，非白名单）/ Charlie 10 / Data API 5 USDC；月预算 50，单笔限额 25。
- 部署 / 本地 env 见根 `.env.example` 与 `frontend/.env.example`。
- 领域术语：mock=不触外部系统；simulation=行为预览非执行；testnet=测试网真实调用；real=真实 provider。Risk Check 是确定性规则（预算 / 白名单 / 限额 / token / 重复），不含 LLM。
- 硬约束（承自原 CONTEXT-MAP，协作方共识）：风控（Risk Check）和审批（Human Approval）不得下放给 LLM；契约以代码 + 测试为准。旧 `CONTEXT-MAP.md` 已删除，`docs/contexts/*.md` 仍可按任务域参考。

## 已知问题

- `frontend/lib/api/*` 端点与后端契约尚未对齐：`NEXT_PUBLIC_DEMO_MODE=real` 前必须重写 adapter，否则请求失败（见 `frontend/.env.example` 内 TODO）。
- 仓库体积：`.claude/` 与 `.agents/` 各 ~83MB、12000+ 文件被 git 跟踪，二者内容完全重复（skills / 图标模板）；`.git` 193MB；`frontend/docs` 49MB、`frontend/public` 45MB。是否移除待主控决策。
- `README.md` 仍引用已移除的 `preview-readme.*`、`docs/outputs/`、`LANGUAGES.md`（悬空链接，待下次 README 整理时清理）。
- 金额字段用 `float`（`app/models.py`），生产化应换 Decimal / 整数最小单位。
- `app/store.py` SQLiteStore 单连接 `check_same_thread=False` 且无锁，并发写有风险（demo 可接受）。
- `GET /api/caw-status/{id}/refresh` 是带副作用的 GET（写 store），HTTP 语义不纯。

## 待确认

- `requirements.txt` 中 `httpx2` / `httpcore2` 非官方包名，需确认是否 `cobo-agentic-wallet` 的真实依赖，评估供应链风险。
- `.claude/`、`.agents/` 重复跟踪资产是否清理（影响 ~166MB 与 24000+ 文件）。
- `.cursor/rules/`、`docs/knowledge/`、`docs/contexts/` 中仍引用已删除的 `docs/agents/*`、`docs/outputs/*`，是否二次清理待定。

## Backlog（低优先）

- `docs/outputs/`（report / prd / handoff / commit-history）旧流程产物已移除，历史记录见 git log。
- refresh 轮询可考虑改为显式 POST 或加节流。
- 后端无 lint / format 配置（ruff 等），可按需补。
