# AgentCFO README image prompts（待补四张说明图）

> Agent **不直接生图**。把本节投喂 GPT Image / img2img；标杆见全局 `readme-polish/references/`。  
> Showcase（`landing-*` / `console-*`）已是真机截图，**不要**用本文 Prompt 重画 UI。

## §0 全局规范

| 项 | 值 |
|---|---|
| 产品 | AgentCFO — DAO AI Treasury |
| 气质 | 深色 command center · 审计 / 风控 / 受控钱包 |
| 色板 | 背景 `#0f172a` · 主强调 lime `#84cc16` · 辅 cyan `#22d3ee` · 警告 amber `#f59e0b` · 危险 coral `#f43f5e` · 文字近白 |
| 硬约束 | 4–6 色；统一描边；正交连线；无金币雨；无假 tx 数字 |
| 命名 | 落盘 `assets/images/readme/{asset}.png` |
| 系统指令（可粘贴） | You design crisp technical README diagrams for a DAO treasury AI product. Flat/semi-flat, 4–6 colors, dark slate background, lime/cyan accents. No crypto meme coins, no illegible micro-text, no fake UI screenshots. |

---

## 1. `features.png`

| 字段 | 内容 |
|---|---|
| 比例 | 16:9 或 2:1 |
| 挂载 | README `#features` |
| 结构 | 2×3 或 3×2 模块卡：Payment Plan · Risk Check · Human Approval · CAW · Audit · Mock Mode |
| 每卡 | 统一线图标 + 短英文标题 + 一行中文或英文说明 |
| English Prompt | Dark slate README features board for AgentCFO. Six equal cards in two rows: AI Payment Plan, Risk Check, Human Approval, CAW Execution, Audit Report, Mock Mode. Lime and cyan accents, consistent stroke icons, generous padding, no fake dashboards, no coin rain. |
| Avoid | 彩虹色块、3D 贴纸、伪 Console 截图 |

## 2. `workflow.png`

| 字段 | 内容 |
|---|---|
| 挂载 | README `#workflow` |
| 结构 | 单主路径六节点：Records → Plan → Risk → Approval → CAW → Audit；Risk 处分叉到 Blocked（次要） |
| English Prompt | Horizontal workflow diagram on dark slate: Contribution Records to AI Payment Plan to Risk Check diamond to Human Approval to Cobo Agentic Wallet to Audit Report. Secondary branch from Risk Check labeled Blocked in coral. Orthogonal arrows, lime nodes, cyan connectors, readable labels only. |
| Avoid | 蜘蛛网连线、超过 2 条主分支 |

## 3. `architecture.png`

| 字段 | 内容 |
|---|---|
| 风格 | client-server 分层（Browser → FastAPI → Planner / Risk / CAW / Store） |
| 挂载 | README `#architecture` |
| English Prompt | Clean layered architecture for AgentCFO. Top: Next.js Browser Console and Landing. Middle: FastAPI API gateway. Bottom services in a row: Payment Planner, Risk Engine, Human Approval Gate, CAW Adapter Mock/Real, SQLite Store, Audit Report. Side note: Agent Chat to MiniMax with no fund authority. Dark slate, lime/cyan, orthogonal only, one style. |
| Avoid | 混用 C4 + 洋葱 + AWS 图标墙 |

## 4. `tech-stack.png`

| 字段 | 内容 |
|---|---|
| 分工 | 只展示技术名分层，不重复 architecture 拓扑 |
| English Prompt | Tech stack strip diagram for AgentCFO. Rows: Frontend Next.js React TypeScript Tailwind; Backend Python FastAPI Pydantic pytest; AI MiniMax and optional OpenAI planner; Data SQLite; Wallet cobo-agentic-wallet. Icon-wall or labeled bands, dark slate, lime accents, real tech names only. |
| Avoid | 与 architecture 同一构图、虚构框架名 |

## Showcase（勿生图）

| 资产 | method |
|---|---|
| `landing-*.png` · `console-*.png` | screenshot（已有） |
| 重截建议 | 本地 `PORT=3100 pnpm dev` 或 Live Demo；UI 大改后再覆盖同名文件 |
