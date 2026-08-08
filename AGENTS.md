# AgentCFO — AI Agent 工作指南

> **Output Style**: `humanizer-tta` skill — 常驻语气人格（Hermes 工程师口吻）+ 成稿去 AI 味。加载路径：`~/.agents/skills/humanizer-tta/SKILL.md` · 仓库细则 `docs/agents/voice.md`
> **Context**: `CONTEXT.md` → `CONTEXT-MAP.md` → `docs/contexts/*`
> **Shared vocab**: 根 `LANGUAGES.md`
> **Windows / Answer / Commit rules**: `.cursor/rules/windows-path-discipline.mdc` · `windows-shell-discipline.mdc` · `answer-format.mdc` · `AGENTS.mdc` · `commit-history.mdc`（从用户级同步，五份必齐）

> 面向所有 AI coding agent 的仓库级说明。Claude Code 用户可同时读 `CLAUDE.md`。

## 单一事实源

| 事实类型 | 唯一入口 |
| --- | --- |
| 领域术语与硬约束 | `CONTEXT.md` + `docs/contexts/*` |
| 共享用词 | `LANGUAGES.md` |
| Agent 硬约束 / 任务流门禁 | 本文件 + `docs/agents/workflow.md` |
| 人读摘要与运行说明 | `README.md` |

禁止维护 `docs/agents/language.md` / `docs/agents/context.md`。流程产物只用 **`docs/outputs/`**（复数）。

## Agent skills

### Issue tracker

GitHub Issues：`https://github.com/San-Y108/agent-cfo/issues`。见 `docs/agents/issue-tracker.md`。

### Triage labels

Matt 五 canonical 状态（`needs-triage` … `wontfix`）。见 `docs/agents/triage-labels.md`。

### Domain docs

多 Context：`CONTEXT-MAP.md` → `docs/contexts/*` + `docs/adr/`。见 `docs/agents/domain.md`。

### 任务流

`Issue → report? → PRD → handoff → 实施 → awaiting-review → commit-history`。细则 `docs/agents/workflow.md` · `deliver.md` · `archive.md`。Bug 八段模板见 `docs/knowledge/project-init.md` §5.0。

## 1. 你在哪个团队？

先确认任务归属，**只在自己目录内改代码**：

| 任务类型 | 去读 | 只改 |
|---|---|---|
| 前端 UI / Console / Landing | `frontend/CLAUDE.md` | `frontend/` |
| 后端 API / 风控 / CAW adapter | 契约短链（下节）+ `docs/backend/` + `app/` | `app/`、`tests/` |
| PM / 排期 / 交付文档 | `docs/README.md` → `docs/pm/` | `docs/`（文字类） |
| 物料 / PPT / 视频 / 截图 | `inbox/README.md` → `assets/README.md` · `ASSET-MAP.md` | 投递放 `inbox/`；归类后只改 `assets/` |
| 合约 / 链上 | 与合约同学对齐 | 团队约定目录 |

前端任务：**不要**用本文件替代 `frontend/CLAUDE.md`。

## 2. 核心业务流程与契约

```text
Contribution Records → Payment Plan → Risk Check → Human Approval
  → Cobo Agentic Wallet → Tx Hash → Audit Report
```

**契约真相（代码 + 测试，勿以文档臆造字段/端点）：**

- `app/models.py`
- `app/routers/payments.py`
- `tests/test_mvp_flow.py`

Agent Hub 聊天：`POST /api/agent/chat` · `app/routers/agent.py` · `app/services/agent_chat.py` · `tests/test_agent_chat.py` · 前端 `frontend/lib/api/agent.ts`。Key 仅在后端 `MINIMAX_API_KEY`。

部署 URL / env 以当前代码、测试与平台控制台为准；文档中的 Render/Vercel 句若与运行时冲突，以可验证运行时为准。

## 3. 仓库地图（治理相关）

```text
agent-cfo/
├── README.md · CONTEXT.md · LANGUAGES.md · AGENTS.md · CLAUDE.md
├── CONTEXT-MAP.md
├── app/ · tests/ · frontend/
├── docs/
│   ├── agents/          workflow · deliver · archive · domain · issue-tracker · triage-labels · voice · port-registry
│   ├── contexts/ · adr/ · knowledge/ · glossary/
│   ├── outputs/         report · prd · handoff · commit-history   ← 流程产物（复数）
│   ├── pm/ · backend/ · plans/ · reports/ · backup/              ← 历史/专项（不机械搬迁）
├── assets/              见 ASSET-MAP（canonical vs 现存物理路径）
├── inbox/
└── .cursor/rules/       五份 MDC（alwaysApply）
```

旧叙事 `docs/output/`（单数）、顶层 `docs/commit-history/`、`docs/images/`：**禁止新建**；已有 stub 重定向到 `docs/outputs/`。

## 4. 常用命令

```bash
# 后端
uvicorn app.main:app --reload --port 8000
pytest

# Agent Hub 聊天冒烟（需 MINIMAX_API_KEY）
curl -X POST http://127.0.0.1:8000/api/agent/chat \
  -H "Content-Type: application/json" \
  -d "{\"messages\":[{\"role\":\"user\",\"content\":\"hi\"}],\"lang\":\"zh\"}"

# 前端（在 frontend/ 下）
PORT=3100 pnpm dev
pnpm typecheck && pnpm build

# README 本地预览壳（非 Preview 站、非 Showcase）
python -m http.server 4173
# → http://127.0.0.1:4173/preview-readme.html

# 代码图谱
npx gitnexus status
npx gitnexus analyze
```

## 5. 交付物速查

| 资产 | 路径（现存物理） | 备注 |
|---|---|---|
| 待归类投递 | `inbox/` | 见 `inbox/README.md` |
| 路演 PPT / 源工程 | `assets/theme/ppt/…` | project-init canonical 目标：`assets/ppt/`；见 `ASSET-MAP.md` |
| 路演讲稿 | `assets/theme/script/` | canonical 目标：`assets/speeches/` |
| 答辩视频 | `assets/video/` | |
| README 图 / Showcase | `assets/images/readme/` | |
| 提交清单 | `docs/pm/SUBMISSION_CHECKLIST.md` | |
| theme 流程产物 | `docs/outputs/{report,prd,handoff}/` | |

新投递目标与债务说明以 `assets/ASSET-MAP.md` 为准（**冲突时以最新 project-init 为准**）。

## Claude Code Skills（工作流）

| Skill | 路径 | 何时用 |
|---|---|---|
| **agent-cfo-monorepo-workflow** | `.claude/skills/agent-cfo-monorepo-workflow/` | 角色边界、跨目录、phase 交接 |
| **frontend-agent-workflow** | `frontend/.claude/skills/frontend-agent-workflow/` | 仅在 `frontend/` |
| **project-init**（全局） | `~/.agents/skills/project-init/` · 仓内副本 `docs/knowledge/project-init.md` | 初始化 / 治理对齐 |
| Matt 系 | `to-prd` · `to-issues` · `triage` · `handoff` · `grill-me` | 任务流；读 `docs/agents/*` |

## 6. 协作原则

- 改 API 前先对齐契约；前端不得发明字段或端点
- 跨目录改动先申请
- 提交前跑对应角色的 typecheck / test / build
- Demo 场景数据全团队一致（Bob = blocked）
- PRD 未批准不写功能代码；Review 先于 commit
- 更新交付物路径时同步 `ASSET-MAP` / 相关索引，不发明第二套事实

## Git Workflow Discipline（全 Agent）

- 多 Agent 并行时，改前先 `git pull origin main`
- **push 前必须检查远端**：`git fetch origin main`，然后 `git log HEAD..origin/main --oneline`
- 若远端有领先提交，必须先 `git pull` 合并后再 push
- 出现冲突时停止，把冲突文件列给用户
- 不要 `--force` push，除非用户明确授权
- commit-history：`docs/outputs/commit-history/{branch}/YYYY-MM-DD.md`（见 `.cursor/rules/commit-history.mdc`）

---

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
