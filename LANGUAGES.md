# Languages and shared vocabulary

## 运行时 / 语言

| 区域 | 语言 / 运行时 | 主要工具 | 验证 |
| --- | --- | --- | --- |
| `frontend/` | TypeScript、TSX、CSS | Next.js 16、React 19、pnpm | `pnpm typecheck`、`pnpm build` |
| `app/`、`tests/` | Python 3 | FastAPI、Pydantic、pytest | `python -m pytest -q` |
| PPT 源工程（现存） | Python、SVG | ppt-master | 见 `assets/theme/ppt/agentcfo-pitch/`；canonical 目标见 `assets/ASSET-MAP.md` |
| 根目录与 `docs/` | Markdown | GFM | README preview shell |
| 配置 | JSON、YAML、MDC | Cursor、Claude Code、Vercel、Render | 语法检查与人工 Review |

## 文案语言

- 项目文档默认中文；
- API 名、字段、命令、错误信息保留英文；
- 对外 README 可保留中英混合的产品名与技术术语；
- Agent 输出语气见 `docs/agents/voice.md`（引用 `humanizer-tta`）。

## 任务流共享词（Agent 必须用）

| 词 | 含义 |
| --- | --- |
| theme | 业务主题目录名，如 `treasury-payout` |
| report | 调研分析，可选，路径 `docs/outputs/report/{theme}/` |
| PRD | 产品需求，`docs/outputs/prd/{theme}/prd.md`；未批准不写功能代码 |
| handoff | 任务交接快照，`docs/outputs/handoff/{theme}/`；覆盖式更新 |
| commit-history | 按分支攒批摘要，`docs/outputs/commit-history/{branch}/` |
| awaiting-review | 实施完成、用户 Review 前停点 |
| Gate | Project Init 或 PRD Review 门禁；Gate 前不大规模业务编码 |

## Preview / Showcase / preview-readme（勿混）

| 产物 | 回答的问题 | 本仓现状 |
| --- | --- | --- |
| **Preview 站** | 仓库有哪些可浏览资产、怎么本地翻？ | 单产品 Web 应用，**通常省略**独立 Preview 站；用 Showcase |
| **Showcase** | 产品主链路长什么样？ | `assets/images/readme/` 下 Landing / Console 截图；README 演示路径 |
| **preview-readme** | README 本身渲染出来长什么样？ | 根 `preview-readme.{html,css,js}`；端口见 `docs/agents/port-registry.md`（4173） |

三者不互相替代。启动 README 壳：仓库根 `python -m http.server 4173` → `http://127.0.0.1:4173/preview-readme.html`（须 HTTP，勿 `file://`）。

## Issue / Triage 用词

- Tracker：GitHub Issues（见 `docs/agents/issue-tracker.md`）
- 五态：`needs-triage` · `needs-info` · `ready-for-agent` · `ready-for-human` · `wontfix`（见 `docs/agents/triage-labels.md`）
- Bug Issue 八段模板：`docs/knowledge/project-init.md` §5.0

## 金额与链上数据

真实资金路径不得依赖 JavaScript 或 Python 浮点语义作为最终账务表示。生产化改造应使用最小单位整数或 `Decimal`，并显式记录 token decimals、chain 和 network。
