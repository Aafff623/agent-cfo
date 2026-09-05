# AgentCFO — AI Agent 工作指南

面向所有 AI coding agent 的仓库级说明。协作 fork（上游 San-Y108/agent-cfo），**改动需克制、可上游化**，不做大规模重构。

## 定位与核心流程

DAO AI 财务官（AI CFO for DAOs）：
`Contribution Records → Payment Plan → Risk Check → Human Approval → Cobo Agentic Wallet → Audit Report`
默认 mock demo；真金路径 opt-in 且 fail-closed。前后端契约唯一真相：`app/models.py`、`app/routers/payments.py`、`tests/test_mvp_flow.py`。风控与人工审批必须始终位于资金执行之前，不得下放给 LLM。

## 结构地图

| 路径 | 内容 |
|---|---|
| `app/` | FastAPI 后端：`routers/`（payments、p2_extensions、agent）+ `services/`（payment_planner、risk_engine、caw_adapter、agent_chat、request_finance） |
| `tests/` | pytest 后端测试 |
| `frontend/` | Next.js 前端（详见 `frontend/CLAUDE.md`） |
| `docs/` | `contexts/`、`adr/`、`backend/` 等真实文档（`docs/outputs/`、`docs/agents/` 等旧流程产物已移除，勿再新建） |
| `assets/`、`inbox/` | 交付资产与待归类投递 |
| `CONTEXT.md` | 真实事实、已知问题、待确认项（先读） |

## 运行与验证（后端依赖见 requirements.txt，需自备 Python 3 环境）

```bash
uvicorn app.main:app --reload --port 8000   # 启动后端（默认 mock）
python -m pytest -q                          # 后端测试
# 前端（在 frontend/ 下）：pnpm install && pnpm dev / pnpm typecheck / pnpm build
```

Agent Hub 聊天需要后端 env `MINIMAX_API_KEY`（见 `.env.example`，勿提交真实 `.env`）。

## 约定

- `temp/`、`.env`、`.codegraph/`、`.gitnexus/`、`*.log` 不入库（见 `.gitignore`）
- 任何密钥 / token / 私钥不入库，一律走环境变量
- 改 API 先对齐契约；前端不得发明字段或端点
- 提交前跑对应侧的 typecheck / test；没跑过就如实说没验证
