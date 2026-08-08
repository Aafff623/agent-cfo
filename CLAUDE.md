# AgentCFO — Claude Code 仓库指南

> **Output Style**: `humanizer-tta` — see `~/.agents/skills/humanizer-tta/SKILL.md` · 仓库细则 `docs/agents/voice.md`
> **Context**: `CONTEXT.md` → `CONTEXT-MAP.md` → `docs/contexts/*`
> **Shared vocab**: 根 `LANGUAGES.md`
> **Windows / Answer / Commit rules**: `.cursor/rules/` 五份 MDC（path · shell · answer-format · AGENTS.mdc · commit-history）

> 团队 monorepo 入口。做**前端**工作时，读完本节后转到 **`frontend/CLAUDE.md`**（前端总纲，优先级更高）。  
> **工作流 Skills**（description Session 常驻，正文动态）：`.claude/skills/agent-cfo-monorepo-workflow/` · `.claude/skills/frontend-agent-workflow/`（`paths: frontend/**`）  
> **加载披露**：`frontend/docs/agent-context-loading.md`  
> **流程产物**：`docs/outputs/{report,prd,handoff,commit-history}/`（复数；旧 `docs/output/` 已废弃）

## Agent skills

### Issue tracker

GitHub Issues。见 `docs/agents/issue-tracker.md`。

### Triage labels

Matt 五态。见 `docs/agents/triage-labels.md`。

### Domain docs

多 Context。见 `docs/agents/domain.md`。

## Context 加载（Claude Code）

| 层级 | 机制 | 是否 Session 必载 |
|---|---|---|
| **宪法** | `CLAUDE.md`（向上 walk cwd；子目录按需） | ✅ 根 `CLAUDE.md`；`frontend/CLAUDE.md` 触达 frontend 或 cwd 在 `frontend/` |
| **Rules** | `.claude/rules/*.md`（可 `paths:`  scoped） | ✅ 无 paths 的规则；`frontend/**` 触达时载入 `rules/frontend.md` |
| **Skill 列表** | `.claude/skills/*/SKILL.md` 的 name + description | ✅ 描述常驻，Agent **知道有哪些 skill** |
| **Skill 正文** | 模型 invoke 或 `/skill-name` | ⚠️ **动态加载**，非全文默认注入 |
| **README** | 非全局；`frontend/CLAUDE.md` 通过 `@README.md` import | frontend 宪法载入时 |

HANDOFF 等状态文件：**不 inject**，由宪法 / rules 要求 Agent **主动 Read**。

README 本地预览：在仓库根运行 `python -m http.server 4173`，打开 `http://127.0.0.1:4173/preview-readme.html`。端口登记见 `docs/agents/port-registry.md`。

## 项目一句话

**AgentCFO ｜ DAO AI 财务官** — 贡献记录 → Payment Plan → Risk Check → Human Approval → Cobo Agentic Wallet → Audit Report。  
赛道：Cobo Agentic Commerce · Slogan: *Give every DAO an AI CFO with a controlled wallet.*

## 仓库结构 & 团队边界

| 角色 | 工作目录 | 入口文档 | 边界 |
|---|---|---|---|
| **PM** | `docs/` | `docs/README.md` · `docs/pm/TASK_BOARD.md` | 文字文档；不改 `app/`、`frontend/` 代码 |
| **物料** | `inbox/` → `assets/` | `inbox/README.md` · `assets/README.md` | 新文件先投 `inbox/`；归类后入 `assets/`，不改业务代码 |
| **前端** | `frontend/` | `frontend/CLAUDE.md` | **只改 `frontend/`**；后端只读契约 |
| **后端** | `app/`、`tests/` | `README.md` · `docs/backend/` | 不改 `frontend/` UI |
| **合约** | （待团队约定） | — | 与 CAW / 链上交互相关 |

```text
docs/     → 文字文档 + agents + contexts + outputs（流程产物）+ pm/backend/plans…
assets/   → 交付资产（物理现状含 theme/ppt·script；canonical 见 assets/ASSET-MAP.md）
inbox/    → 待归类投递（整理后迁入 assets/ 或 docs/）
frontend/docs/ → 前端开发专项文档（与竞赛交付文档分开）
```

README 首页已于 2026-06-13 按 [`docs/plans/README-merge-plan.md`](docs/plans/README-merge-plan.md) 合并；合并前完整技术版见 [`docs/backup/README-20260613-pre-polish.md`](docs/backup/README-20260613-pre-polish.md)。

全 agent 通用指南见 **`AGENTS.md`**。

**跨边界规则**：修改非本角色目录前，先与对应队友确认或向用户申请。

## 新会话阅读顺序

### 全仓库概览（任何角色）

1. 启用 skill **`agent-cfo-monorepo-workflow`**（`.claude/skills/agent-cfo-monorepo-workflow/`）
2. `README.md` — 项目首页、Demo、Quick Start、API 摘要（深文档见 `docs/backend/`）
3. `AGENTS.md` — 全 agent 仓库地图与 GitNexus 纪律
4. 本文件 — Claude Code 团队边界
5. `docs/README.md` / `assets/README.md` / `inbox/README.md` — 文档、交付资产与投递区入口
6. 本角色专属文档（见上表）

README 合并记录：[`docs/plans/README-merge-plan.md`](docs/plans/README-merge-plan.md) · 备份：[`docs/backup/README-20260613-pre-polish.md`](docs/backup/README-20260613-pre-polish.md)

### 前端开发（我们）

1. 启用 skill **`frontend-agent-workflow`**（根 `.claude/skills/frontend-agent-workflow/`）
2. **`frontend/CLAUDE.md`** — 总纲（必读）
3. `frontend/HANDOFF.md` → 最新 `frontend/docs/handoff/*`
4. `frontend/docs/plans/console-upgrade-checklist.md`
5. `frontend/backend-integration.md`（联调时）

### 物料开发

1. `inbox/README.md` — 队友新投递的待归类文件
2. `assets/README.md` — 已入库交付资产与状态
3. `docs/pm/SUBMISSION_CHECKLIST.md` — 提交项勾选
4. `.claude/skills/ppt-master/SKILL.md` — 修改或重新导出 ppt-master 版 PPT 时

### 后端开发

1. `app/models.py` · `app/routers/payments.py` · `tests/test_mvp_flow.py`
2. `docs/backend/` — CAW、部署、env、P2 技术深文档（合并后；当前见根目录 `README.md`）
3. `docs/pm/P2_BACKEND_READINESS.md`（如有）

## API 契约（全团队共用）

**唯一真相源**（前后端分歧时以后端代码为准）：

- `app/models.py`
- `app/routers/payments.py`
- `tests/test_mvp_flow.py`

P0 端点（4+1）+ Agent 聊天：

| 方法 | 路径 |
|---|---|
| POST | `/api/payment-plan` |
| POST | `/api/risk-check` |
| POST | `/api/execute-payment` |
| GET | `/api/audit-report/{auditReportId}` |
| GET | `/api/caw-status/{cawRequestId}` |
| POST | `/api/agent/chat` |

Agent Hub 聊天经后端代理 [MiniMax OpenAI 兼容 API](https://platform.minimaxi.com/docs/guides/models-intro)。Render / 本地配置 `MINIMAX_API_KEY`（可选 `MINIMAX_BASE_URL`、`MINIMAX_MODEL`）。**不依赖** Treasury mock/real 模式。

前端 adapter 镜像：`frontend/lib/api/*` · 禁止自行发明 endpoint / field / wrapper。

## 当前部署

| 层 | URL / 状态 |
|---|---|
| 前端（Vercel） | https://agentcfo-frontend.vercel.app · mock mode |
| 后端（Render） | https://agentcfo-backend.onrender.com · 默认 mock mode |
| 本地后端 | `uvicorn app.main:app --reload --port 8000` |
| 产品入口 | `/` Landing · `/console` Command Center |

## 竞赛交付物

| 资产 | 路径（现存物理） |
|---|---|
| 待归类投递 | `inbox/` |
| 路演 PPT（ppt-master） | `assets/theme/ppt/agentcfo-pitch.pptx`（canonical 目标 `assets/ppt/`，见 `ASSET-MAP.md`） |
| 路演 PPT（物料同学 PDF） | `assets/theme/ppt/material/agentcfo-pitch-material-team-v1.pdf` |
| PPT 源工程 | `assets/theme/ppt/agentcfo-pitch/` |
| 答辩视频 | `assets/video/`（公开链接写入 `README.md` § Demo Video） |
| 提交清单 | `docs/pm/SUBMISSION_CHECKLIST.md` |
| README 合并规划 | `docs/plans/README-merge-plan.md` |
| README 展示用图 / Showcase | `assets/images/readme/` |
| theme 流程产物 | `docs/outputs/{report,prd,handoff}/` |

## Demo 数据（全团队对齐）

Alice 20 / **Bob 15（blocked，非白名单）** / Charlie 10 / Data API 5 USDC · 月预算 50 · 单笔限额 25

## 代码探索（GitNexus）

仓库已索引 GitNexus。探索跨模块代码、影响面分析时，见根目录 **`AGENTS.md`** § GitNexus。  
索引过期：`npx gitnexus analyze`（在仓库根执行）。

## 安全 & Demo 纪律

- 黑客松 Demo；mock mode 无真实资金
- 不把 mock tx 当作真实链上交易
- 不伪造验证结果；没跑就是没验证

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **agent-cfo** (4819 symbols, 8434 relationships, 162 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/agent-cfo/context` | Codebase overview, check index freshness |
| `gitnexus://repo/agent-cfo/clusters` | All functional areas |
| `gitnexus://repo/agent-cfo/processes` | All execution flows |
| `gitnexus://repo/agent-cfo/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->
