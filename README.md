<p align="center">
  <img src="assets/images/readme/banner.png" alt="AgentCFO — AI CFO for Web3 Treasury team banner" width="100%">
</p>

<h1 align="center">AgentCFO — DAO AI Treasury</h1>

<p align="center"><em>Give every DAO an AI CFO with a controlled wallet</em></p>

<p align="center">
  面向 Web3 小团队 / DAO 的 AI 财务官：贡献记录 → Payment Plan → Risk Check → Human Approval → <strong>Cobo Agentic Wallet (CAW)</strong> → Audit Report。<br>
  默认 <strong>mock demo</strong>；真金路径 opt-in 且 fail-closed。
</p>

<p align="center">
  <a href="https://agentcfo-frontend.vercel.app"><img src="https://img.shields.io/badge/Demo-Live-059669?style=for-the-badge&labelColor=0f172a" alt="Live Demo"></a>
  <a href="https://agentcfo-backend.onrender.com/health"><img src="https://img.shields.io/badge/API-Render-3B82F6?style=for-the-badge&labelColor=0f172a" alt="Backend"></a>
  <a href="https://github.com/Aafff623/agent-cfo/wiki"><img src="https://img.shields.io/badge/Wiki-Handbook-8b5cf6?style=for-the-badge&labelColor=0f172a" alt="Wiki"></a>
  <img src="https://img.shields.io/badge/Mode-mock--default-f59e0b?style=for-the-badge&labelColor=0f172a" alt="Mock default">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License">
  <a href="https://github.com/Aafff623/agent-cfo"><img src="https://img.shields.io/github/stars/Aafff623/agent-cfo.svg?style=for-the-badge" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="#project">Project</a>
  · <a href="#features">Features</a>
  · <a href="#showcase">Showcase</a>
  · <a href="#quick-start">Quick start</a>
  · <a href="#workflow">Workflow</a>
  · <a href="#architecture">Architecture</a>
  · <a href="#repo-structure">Repo structure</a>
  · <a href="#api-参考">API</a>
  · <a href="#文档">Docs</a>
  · <a href="https://github.com/Aafff623/agent-cfo/wiki">Wiki</a>
  · <a href="#团队">Team</a>
</p>

---

## Project

本仓库是黑客松原版 [San-Y108/agent-cfo](https://github.com/San-Y108/agent-cfo) 的 **个人维护 fork**，由 [@Aafff623](https://github.com/Aafff623)（**threetwoa**）托管，用于赛后个性化二开。

| 项 | 说明 |
|---|---|
| **当前主仓** | [`Aafff623/agent-cfo`](https://github.com/Aafff623/agent-cfo) |
| **主维护者** | threetwoa — Landing / Console、README 与配图叙事、Demo 视频、本 fork 演进 |
| **上游** | 保留小队协作与赛道叙事；日常开发以本仓为准 |
| **README 范式** | 对齐 [fork-Firefly](https://github.com/Aafff623/fork-Firefly) 的章节节奏 + 本仓黑客松级 Showcase 密度 |
| **Preview 产品壳** | **无**独立 Preview 站（单产品）；产品面见 [Showcase](#showcase)。README 本地预览壳是 [`preview-readme.html`](preview-readme.html)（端口 **4173**），与 Console 无关 |
| **Wiki / 说明书** | [GitHub Wiki](https://github.com/Aafff623/agent-cfo/wiki)；产品 Live 仍用现有 Vercel，不另开文档站 |

硬边界：**LLM 不做授权**；Risk Engine 是唯一 `Ready` / `NeedsApproval` / `Blocked` 裁决层；blocked 项不进 CAW；mock tx ≠ 链上交易。

---

## 为什么需要 AgentCFO

DAO 小团队常碰到：

- 贡献结算靠表格 → 漏发、错发、重复发
- 支出不透明 → 事后难审计
- 多签太重 / 全自动太险 → 缺「受控自动化」中间态

| 组件 | 职责 |
|---|---|
| Agent / LLM | 整理贡献、生成计划与原因说明 |
| Risk Engine | 预算 / 白名单 / 限额 / 重复付款（确定性） |
| Human Approval | 关键确认；blocked 不可执行 |
| CAW Adapter | 隔离 Cobo Agentic Wallet 调用 |
| Audit Report | 计划 · 风险 · 审批 · 执行结果可追溯 |

---

## Features

| Area | Capability | Entry |
|---|---|---|
| **AI Payment Plan** | 贡献记录 → 结构化付款计划与原因 | `POST /api/payment-plan` · Console Treasury |
| **Agent Hub Chat** | 后端代理 MiniMax；Key 不进前端 | `POST /api/agent/chat` · `/console` |
| **Risk Check** | 预算、白名单、单笔限额、token、重复付款 | `POST /api/risk-check` |
| **Human Approval** | 执行前必须人工确认 | Console Approval 闸门 |
| **CAW Execution** | 真付款路径必经 CAW；默认 mock | `POST /api/execute-payment` |
| **Audit Report** | 原因、风险、状态、剩余预算、tx / request id | `GET /api/audit-report/{id}` |
| **Mock Mode** | 全链路可演示；必须标明 mock | `CAW_ADAPTER_MODE=mock`（默认） |

> 契约说明图 `features.png` / `workflow.png` / `architecture.png` / `tech-stack.png` 待按 [readme-polish](docs/outputs/prd/readme-diagrams/readme-diagram-brief.md) 补齐；**Showcase 截图已齐**，勿用说明图冒充 UI。

**Cobo Agentic Commerce 对齐（摘要）**

| 方向 | 本项目如何体现 |
|---|---|
| Agent-Native Payments | 计划生成 + 规则内发起受控付款 |
| Agent Resource Procurement | Demo 含 Data API 订阅结算 |
| A2A Economy / Treasury | P2 multi-agent 预算模拟（demo-safe，默认非 live） |

---

## Showcase

本仓无独立 Preview 产品站；下表即主链路真机面（Landing + Console）。截图来自 Live Demo / 本地 Console，文件名沿用产品分区前缀（`landing-*` · `console-*`），气质对齐 fork-Firefly 的 `showcase-*` 规范：**真机 UI，禁止文生图冒充**。

### Demo 场景

| 对象 | 类型 | 说明 | 金额 |
|---|---|---|---|
| Alice | 贡献者 | 活动复盘 | 20 USDC |
| Bob | 贡献者 | 海报设计（**白名单外 → blocked**） | 15 USDC |
| Charlie | 贡献者 | 社群与数据 | 10 USDC |
| Data API | 工具订阅 | 本月服务费 | 5 USDC |

月预算 **50 USDC** · 单笔限额 **25 USDC**。Bob blocked；其余经 Human Approval 后可执行（mock 默认）。

### Landing

<table>
  <tr>
    <td width="33%" valign="top">
      <a href="assets/images/readme/landing-hero.png"><img alt="Landing Hero" src="assets/images/readme/landing-hero.png" width="100%"></a>
      <p><strong>Hero</strong> · 价值主张与 CTA<br><a href="https://agentcfo-frontend.vercel.app">Live</a></p>
    </td>
    <td width="33%" valign="top">
      <a href="assets/images/readme/landing-pipeline.png"><img alt="Pipeline" src="assets/images/readme/landing-pipeline.png" width="100%"></a>
      <p><strong>Pipeline</strong> · Plan → Risk → Approval → CAW → Audit</p>
    </td>
    <td width="33%" valign="top">
      <a href="assets/images/readme/landing-platform.png"><img alt="Platform" src="assets/images/readme/landing-platform.png" width="100%"></a>
      <p><strong>Platform</strong> · 模块边界</p>
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <a href="assets/images/readme/landing-guardrails.png"><img alt="Guardrails" src="assets/images/readme/landing-guardrails.png" width="100%"></a>
      <p><strong>Guardrails</strong> · 预算 / 白名单 / fail-closed</p>
    </td>
    <td width="33%" valign="top">
      <a href="assets/images/readme/landing-timelines.png"><img alt="Timelines" src="assets/images/readme/landing-timelines.png" width="100%"></a>
      <p><strong>Timelines</strong> · scaffold → testnet evidence</p>
    </td>
    <td width="33%" valign="top">
      <a href="assets/images/readme/landing-faq.png"><img alt="FAQ" src="assets/images/readme/landing-faq.png" width="100%"></a>
      <p><strong>FAQ</strong> · 评委常见问题</p>
    </td>
  </tr>
</table>

### Console Command Center

推荐路径：`/console` → Treasury →（可选）Agent Hub / Policy / Wallets / Analytics

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="assets/images/readme/console-agent-hub.png"><img alt="Agent Hub" src="assets/images/readme/console-agent-hub.png" width="100%"></a>
      <p><strong>Agent Hub</strong> · <a href="https://agentcfo-frontend.vercel.app/console">/console</a></p>
    </td>
    <td width="50%" valign="top">
      <a href="assets/images/readme/console-treasury.png"><img alt="Treasury" src="assets/images/readme/console-treasury.png" width="100%"></a>
      <p><strong>Treasury</strong> · <a href="https://agentcfo-frontend.vercel.app/console/treasury">/console/treasury</a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="assets/images/readme/console-wallets.png"><img alt="Wallets" src="assets/images/readme/console-wallets.png" width="100%"></a>
      <p><strong>CAW Wallets</strong> · <a href="https://agentcfo-frontend.vercel.app/console/wallets">/console/wallets</a></p>
    </td>
    <td width="50%" valign="top">
      <a href="assets/images/readme/console-analytics.png"><img alt="Analytics" src="assets/images/readme/console-analytics.png" width="100%"></a>
      <p><strong>Analytics</strong> · <a href="https://agentcfo-frontend.vercel.app/console/analytics">/console/analytics</a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="assets/images/readme/console-policy.png"><img alt="Policy" src="assets/images/readme/console-policy.png" width="100%"></a>
      <p><strong>Policy</strong> · <a href="https://agentcfo-frontend.vercel.app/console/policy">/console/policy</a></p>
    </td>
    <td width="50%" valign="top">
      <a href="assets/images/readme/landing-footer.png"><img alt="Footer CTA" src="assets/images/readme/landing-footer.png" width="100%"></a>
      <p><strong>Landing CTA</strong> · 进入 Console</p>
    </td>
  </tr>
</table>

### Demo Video

**[▶ 在线观看](https://agentcfo-frontend.vercel.app/#guardrails)** — Landing `#guardrails`（<2 min：Plan → Risk → Approval → CAW → Audit）。

源文件：[`assets/video/agentcfo-demo.mp4`](assets/video/agentcfo-demo.mp4) · 路演 PPT：[`assets/theme/ppt/agentcfo-pitch.pptx`](assets/theme/ppt/agentcfo-pitch.pptx)（物理路径；canonical 目标见 [`assets/ASSET-MAP.md`](assets/ASSET-MAP.md)）

---

## Quick start

### 30 秒看 Demo（前端 mock）

```bash
git clone https://github.com/Aafff623/agent-cfo.git
cd agent-cfo/frontend
pnpm install
PORT=3100 pnpm dev
```

打开 [http://localhost:3100/console](http://localhost:3100/console)。**请用 3100**（3001 易撞陈旧 Service Worker 白屏）。

### 常用命令

| 命令 | 作用 |
|---|---|
| `PORT=3100 pnpm dev`（在 `frontend/`） | 前端 mock Console |
| `python -m uvicorn app.main:app --reload`（仓根 · venv） | 本地后端 `:8000` |
| `pytest -q` | P0 验收 |
| `python -m http.server 4173`（仓根） | README 预览壳 → http://127.0.0.1:4173/preview-readme.html |
| `curl https://agentcfo-backend.onrender.com/health` | 线上 API 探活 |

### 验证线上后端

```bash
curl https://agentcfo-backend.onrender.com/health
curl https://agentcfo-backend.onrender.com/api/demo-sample
```

预期：`{"status":"ok","service":"agent-cfo-backend"}`

| 项目 | 当前值 |
|---|---|
| API mode | `mock-demo` |
| CAW mode | `mock`（Render 默认） |
| P0 flow | `payment-plan → risk-check → execute-payment → audit-report` |

<details>
<summary>Windows / macOS 本地后端 · 联调 · CAW real · env</summary>

**Windows**

```powershell
git clone https://github.com/Aafff623/agent-cfo.git
cd agent-cfo
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pytest -q
.venv\Scripts\python -m uvicorn app.main:app --reload
```

**macOS / Linux**

```bash
git clone https://github.com/Aafff623/agent-cfo.git
cd agent-cfo
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q
.venv/bin/python -m uvicorn app.main:app --reload
```

| 场景 | 说明 |
|---|---|
| 前端 real 联调 | `NEXT_PUBLIC_DEMO_MODE=real` + `NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000` |
| CAW real | `CAW_ADAPTER_MODE=real` + `CAW_ENABLE_TRANSFERS=true` + 全套 CAW env（fail-closed） |
| Agent Hub | `MINIMAX_API_KEY`（仅后端） |
| 文档 | [`docs/backend/ENV_VARS.md`](docs/backend/ENV_VARS.md) · [`docs/backend/CAW_ADAPTER.md`](docs/backend/CAW_ADAPTER.md) · [`docs/backend/DEPLOYMENT.md`](docs/backend/DEPLOYMENT.md) |

**安全：** 不提交 `.env` / API key / pact-scoped key；不把 mock tx 当链上交易。

</details>

### 阅读顺序

| 顺序 | 路径 | 目的 |
|---|---|---|
| 1 | `README.md` | 产品、Demo、边界 |
| 2 | `AGENTS.md` / `CLAUDE.md` | 目录职责与任务流 |
| 3 | `app/` + `tests/` | P0 契约 |
| 4 | `frontend/CLAUDE.md` | 仅前端同学 |
| 5 | `docs/` · `assets/` | 深文档与交付物 |

---

## Workflow

```text
Contribution Records
  → AI Payment Plan          (LLM / mock planner：说明与结构化计划)
  → Risk Check               (确定性引擎：唯一裁决 Ready / NeedsApproval / Blocked)
  → Human Approval           (人工闸门；blocked 止步)
  → Cobo Agentic Wallet      (Mock 默认 · Real testnet opt-in)
  → Tx / request id
  → Audit Report             (执行时快照；后续 status refresh 不改写)
```

| 步骤 | 谁说了算 | 反模式 |
|---|---|---|
| 计划 | Planner 可写 summary/reason | 改金额 / 钱包 / 风险结论 |
| 风控 | `risk_engine` | 让 LLM「觉得可以付」 |
| 执行 | `humanApproval.approved` + 非 blocked | 跳过审批直打 CAW |
| 审计 | 快照落库 | 用后续 CAW poll 偷偷改 Audit |

---

## Architecture

```text
Browser (Next.js · Landing + Console)
  → DEMO_MODE=mock  → frontend/lib/mock + console-state
  → DEMO_MODE=real  → frontend/lib/api/* → FastAPI
       → payment_planner → store
       → risk_engine     → store
       → (approval) → caw_adapter → store + AuditReport
       → agent_chat      → MiniMax（无资金权限）
```

| 层 | 技术 | 部署 |
|---|---|---|
| Frontend | Next.js 16 · React 19 · TypeScript · Tailwind v4 | [Vercel](https://agentcfo-frontend.vercel.app)（mock） |
| Backend | Python · FastAPI · Pydantic · pytest · SQLite | [Render](https://agentcfo-backend.onrender.com)（mock） |
| CAW | `cobo-agentic-wallet==0.1.40` | Mock 默认 · Real testnet opt-in |

**关键原则**

- Risk Engine 唯一决定 `Ready` / `NeedsApproval` / `Blocked`
- Execute 必须 `humanApproval.approved=true`；blocked 不进 adapter
- Audit Report 为执行时快照
- RealCawAdapter 缺 env / allowlist / policy → fail closed
- Read-only observer 只查询，不转账

详见 [`docs/backend/CAW_ADAPTER.md`](docs/backend/CAW_ADAPTER.md)。

### Tech stack

| 层 | 选型 |
|---|---|
| UI | Next.js App Router · React 19 · Tailwind CSS v4 · Framer Motion / GSAP · recharts |
| API | FastAPI · Pydantic · uvicorn · pytest |
| AI | Payment Plan：mock / 可选 OpenAI structured；Agent Hub：MiniMax（后端代理） |
| Data | SQLite（默认）· 可切 memory store |
| Wallet | Cobo Agentic Wallet SDK · MockCawAdapter / RealCawAdapter |

### CAW Testnet 证据（公开脱敏）

> 来源：CAW/合约（purple sun）于 2026-06-10 提供的 Phase 4C 闭环证据。API Key / pact-scoped key 永不入库；线上 Render 仍默认 `mock`，本节**只展示公开链上事实**。

#### Agent Wallet（公开信息）

| 字段 | 值 |
|---|---|
| Network / Token | Sepolia / `SETH` |
| Agent Wallet | `0x2cda2abddfcc7b8a59b7dfa9c4d8855f6bd576da`（`0x2cda...76da`） |
| CAW Wallet ID | `36bca6d8-1273-4d85-b099-6eca490e966f` |

#### 证据 1：Demo payment

| 字段 | 值 |
|---|---|
| amount | `0.001` SETH |
| txHash | [`0x85a5…4d98`](https://sepolia.etherscan.io/tx/0x85a5a2e934ca0e34c7fb3e038ca06e54e15bd29b56b64e5b01ff80eb20ed4d98) |
| provider status | `900`（Success） |
| Purpose | 对外转账通路全链路验证 |
| Date (UTC) | 2026-06-09 07:56 |

#### 证据 2：Internal transfer

| 字段 | 值 |
|---|---|
| amount | `0.001` SETH |
| txHash | [`0x6bd7…ae8a`](https://sepolia.etherscan.io/tx/0x6bd793bc3030c995245b2e73a466898e46278be092aa9f7a3c86cad21cbbae8a) |
| Purpose | 同 Agent Wallet 内部路由（**不替代** Demo payment） |
| Date (UTC) | 2026-06-09 01:45 |

完整字段见 [`docs/backend/CAW_ADAPTER.md`](docs/backend/CAW_ADAPTER.md)。

---

## Repo structure

```text
agent-cfo/
├── README.md                 # 本文件（人类入口）
├── AGENTS.md · CLAUDE.md     # Agent 治理
├── CONTEXT.md · LANGUAGES.md
├── app/                      # FastAPI 后端（勿与 frontend/app 混淆）
├── tests/                    # pytest · P0 契约
├── frontend/                 # Next.js · Landing + Console
├── docs/
│   ├── agents/               # workflow · triage · deliver …
│   ├── backend/              # CAW / ENV / Deploy / P2
│   ├── contexts/             # 多 Context
│   ├── outputs/              # report · prd · handoff · commit-history
│   └── knowledge/            # 可迁移规范（含 project-init 副本）
├── assets/
│   ├── images/readme/        # Banner · Showcase 截图
│   ├── video/                # Demo 视频
│   └── theme/ppt/            # 路演物料（物理债务路径，见 ASSET-MAP）
├── inbox/                    # 待归类投递
├── preview-readme.html       # README 本地预览壳（4173）
└── .github/                  # Issue / PR 薄模板
```

契约真相：`app/models.py` · `app/routers/payments.py` · `tests/test_mvp_flow.py`

---

## Style and assets

对齐 [fork-Firefly](https://github.com/Aafff623/fork-Firefly) + [readme-polish](https://github.com/Aafff623/agent-cfo/blob/main/docs/knowledge/readme-polish/SKILL.md) 配图契约：

| 资产 | 约定 | 本仓状态 |
|---|---|---|
| `banner.png` | 页首横幅 · 约 3:1 | ✅ |
| `features.png` · `workflow.png` · `architecture.png` · `tech-stack.png` | 说明图 · 4–6 色 · 非 UI 冒充 | ⏳ 待补（brief/prompts 见 `docs/outputs/prd/readme-diagrams/`） |
| `landing-*.png` · `console-*.png` | **Showcase 真机截图**（本仓命名；Firefly 用 `showcase-*`） | ✅ |
| `preview-shell.png` | Preview 产品壳 | ⊘ 本仓无 Preview 站，不强制 |
| `preview-readme.html` | README 排版预览壳 | ✅ 端口 **4173** |
| 终稿目录 | **仅** `assets/images/readme/` | ✅ 禁止 `docs/images/` |

规则：真机 Showcase；mock/testnet/real 可辨；替换保持文件名；不提交密钥或未脱敏截图。详见 [`assets/images/readme/README.md`](assets/images/readme/README.md)。

---

## API 参考

### P0 核心端点

| Endpoint | Method | 说明 |
|---|---|---|
| `/api/payment-plan` | POST | 贡献记录 + 预算 → Payment Plan |
| `/api/risk-check` | POST | 确定性风险检查 |
| `/api/execute-payment` | POST | 人工确认后经 CAW 执行 |
| `/api/audit-report/{auditReportId}` | GET | Audit Report |
| `/api/caw-status/{cawRequestId}` | GET | mock / CAW 请求状态 |
| `/api/agent/chat` | POST | Agent Hub（MiniMax 代理） |

契约：`app/models.py` · `app/routers/payments.py` · `app/routers/agent.py` · `tests/test_mvp_flow.py` · `tests/test_agent_chat.py`

<details>
<summary>curl 验证示例（本地 mock）</summary>

```bash
curl.exe -X POST http://127.0.0.1:8000/api/payment-plan -H "Content-Type: application/json" -d "{\"contributions\":[{\"name\":\"Alice\",\"role\":\"Content Contributor\",\"task\":\"Wrote event recap article\",\"wallet\":\"0xAlice\",\"amount\":20,\"token\":\"USDC\"}],\"budgetRule\":{\"monthlyBudget\":50,\"singlePaymentLimit\":25,\"allowedToken\":\"USDC\",\"whitelist\":[\"0xAlice\"],\"requiresHumanApproval\":true}}"
```

更多见 [`docs/backend/TESTING.md`](docs/backend/TESTING.md)。

</details>

<details>
<summary>P2 扩展 API（demo-safe）</summary>

P2 为 metadata / preview / simulation，不改变 P0 授权与 Audit 不可变性。见 [`docs/backend/P2_APIS.md`](docs/backend/P2_APIS.md)。

</details>

### 验收要点

- 预算 / 白名单 / 单笔限额 / 重复付款 → block  
- 缺 human approval → 不执行  
- Blocked → 不进 CAW adapter  
- Mock execution → 明确 `mode="mock"`

---

## 路线图

| 阶段 | 状态 | 要点 |
|---|---|---|
| **P0** | ✅ | 核心 API · Risk Engine · Mock CAW · Audit · Real skeleton |
| **P1** | ✅ | Render · SQLite · CAW status · 运行说明 |
| **P2** | ✅ demo-safe | External refs · RF/Sablier/Safe mock · multi-agent treasury sim |
| **P2 live** | 🔜 需批准 | 真实外部集成默认关闭 |
| **Fork 演进** | 🔄 | 个人维护仓治理 / README 范式 / Console 体验持续迭代 |

---

## 文档

| 文档 | 说明 |
|---|---|
| [GitHub Wiki](https://github.com/Aafff623/agent-cfo/wiki) | 评委 / 试用者手册（Demo · FAQ · Console）；**不**另挂 Vercel 文档站 |
| [`CONTEXT.md`](CONTEXT.md) · [`CONTEXT-MAP.md`](CONTEXT-MAP.md) | 领域事实与多 Context 路由 |
| [`AGENTS.md`](AGENTS.md) · [`CLAUDE.md`](CLAUDE.md) | Agent 工作指南 |
| [`docs/backend/`](docs/backend/README.md) | CAW · 部署 · env · P2 · 测试 |
| [`docs/outputs/`](docs/outputs/README.md) | report · prd · handoff · commit-history |
| [`frontend/README.md`](frontend/README.md) | 前端开发与 mock/real |
| [`frontend/backend-integration.md`](frontend/backend-integration.md) | 联调 |
| [`assets/ASSET-MAP.md`](assets/ASSET-MAP.md) | 资产 canonical vs 物理路径 |
| [`docs/pm/`](docs/pm/) | 看板 · 提交清单 · 彩排 |
| [`docs/backup/README-20260808-pre-firefly-align.md`](docs/backup/README-20260808-pre-firefly-align.md) | 本轮 README 重组前备份 |

**纪律：** README = 人类入口；`docs/` = 文字；`assets/` = 已归类交付物；`inbox/` = 待投递。API 以代码与 pytest 为准。

---

## 团队

### 本仓维护（fork 后）

| Avatar | 姓名 | 角色 | 职责 | 3D 形象 |
|---|---|---|---|---|
| <a href="assets/images/avatar/threetwoa-role.jpg"><img src="assets/images/avatar/threetwoa-role.jpg" width="80" alt="threetwoa"></a> | **[threetwoa](https://github.com/Aafff623)** | **主维护 · 二开** | 本 fork；Landing / Console；README 与配图；Demo 视频；赛后迭代 | <a href="assets/images/avatar/threetwoa-mascot.png"><img src="assets/images/avatar/threetwoa-mascot.png" width="100" alt="threetwoa 3D"></a> |

### 黑客松参赛小队（致谢）

| Avatar | 姓名 | 角色 | 职责 | 3D 形象 |
|---|---|---|---|---|
| <a href="assets/images/avatar/zanyk-role.jpg"><img src="assets/images/avatar/zanyk-role.jpg" width="80" alt="ZanyK"></a> | **ZanyK** | 指导 / 交付总控 | 统筹、路演、GitHub、交付 | <a href="assets/images/avatar/zanyk-mascot.png"><img src="assets/images/avatar/zanyk-mascot.png" width="100" alt="ZanyK 3D"></a> |
| <a href="assets/images/avatar/huan-role.jpg"><img src="assets/images/avatar/huan-role.jpg" width="80" alt="欢"></a> | **欢** | PM | 需求、路线、站会 | <a href="assets/images/avatar/huan-mascot.png"><img src="assets/images/avatar/huan-mascot.png" width="100" alt="欢 3D"></a> |
| <a href="assets/images/avatar/guagua-role.jpg"><img src="assets/images/avatar/guagua-role.jpg" width="80" alt="呱呱"></a> | **呱呱** | 物料 / 设计 | PPT、海报、文案、视觉 | <a href="assets/images/avatar/guagua-mascot.png"><img src="assets/images/avatar/guagua-mascot.png" width="100" alt="呱呱 3D"></a> |
| <a href="assets/images/avatar/threetwoa-role.jpg"><img src="assets/images/avatar/threetwoa-role.jpg" width="80" alt="threetwoa"></a> | **[threetwoa](https://github.com/Aafff623)** | 前端 · README · Demo | Landing + Console、README、视频 | <a href="assets/images/avatar/threetwoa-mascot.png"><img src="assets/images/avatar/threetwoa-mascot.png" width="100" alt="threetwoa 3D"></a> |
| <a href="assets/images/avatar/jiujiu-role.jpg"><img src="assets/images/avatar/jiujiu-role.jpg" width="80" alt="九九八乂"></a> | **九九八乂** | 后端 / Agent | FastAPI、Plan、Risk、Audit | <a href="assets/images/avatar/jiujiu-mascot.png"><img src="assets/images/avatar/jiujiu-mascot.png" width="100" alt="九九八乂 3D"></a> |
| <a href="assets/images/avatar/purple-sun-role.jpg"><img src="assets/images/avatar/purple-sun-role.jpg" width="80" alt="purple sun"></a> | **purple sun** | 合约 / CAW | CAW 集成、测试网证据 | <a href="assets/images/avatar/purple-sun-mascot.png"><img src="assets/images/avatar/purple-sun-mascot.png" width="100" alt="purple sun 3D"></a> |

<details>
<summary>赛事 · 赛程 · Cobo 赛道匹配（黑客松归档）</summary>

[AI × Web3 Agentic Builders Hackathon](https://casualhackathon.com) — Cobo 赛道｜Agentic Economy × CAW。队名：AgentCFO \| 链上财务官小队。Build 2026-06-01 — 06-12；提交截止 06-13；Demo Day 06-14。

| 方向 | 体现 |
|---|---|
| Agent-Native Payments | 计划 + 受控付款 |
| Agent Resource Procurement | Data API 订阅 Demo |
| A2A Economy / Treasury | P2 multi-agent 模拟 + Human Approval 边界 |

技术生态：Cobo Agentic Wallet（执行核心）· Request Finance / Sablier / Safe（P2 preview，默认非 live）。

</details>

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Aafff623/agent-cfo&type=Date)](https://star-history.com/#Aafff623/agent-cfo&Date)

## 许可证

[MIT](LICENSE)

---

Maintained by [threetwoa](https://github.com/Aafff623) · README style aligned with [fork-Firefly](https://github.com/Aafff623/fork-Firefly) · hackathon credits to ZanyK · 欢 · 呱呱 · 九九八乂 · purple sun
