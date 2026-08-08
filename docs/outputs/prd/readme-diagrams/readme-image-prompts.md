# AgentCFO README image prompts

## 0. 全局规范

项目：AgentCFO，DAO AI Treasury。

视觉总调：dark command center，charcoal background，lime primary accent，cyan/blue/violet/coral status accents，flat technical UI，precise grid，subtle glass panels，no decorative crypto coins。

证据规则：

- mock 不显示真实 txHash；
- testnet 必须标 network；
- 不生成 API key、私钥、二维码或虚构余额；
- 不声称 mainnet、production 或 tamper-proof，除非输入材料提供证据。

命名：

```text
banner.png
features.png
architecture.png
tech-stack.png
workflow.png
structure.png
preview-shell.png
showcase-<name>.png
```

### 给图像模型的系统指令

```text
Create a documentation illustration for AgentCFO, a controlled DAO treasury agent.
Use the supplied screenshot as the factual source. Preserve all product names and
status labels. Do not invent transaction hashes, balances, wallet addresses, or
live integrations. Render a dark editorial command-center aesthetic with a strict
grid, lime accent, and restrained cyan, blue, violet, and coral semantic colors.
No gradients, coin imagery, cyberpunk clutter, or marketing superlatives.
```

## 1. banner.png

- 比例：3:1
- 描述：AgentCFO 品牌横幅，突出 controlled wallet 与 policy-enforced payout flow
- 元素：AgentCFO 标题、Contribution → Plan → Risk → Approval → CAW → Audit

```text
Wide 3:1 documentation banner for "AgentCFO — DAO AI Treasury".
Centered product name, compact subtitle "Give every DAO an AI CFO with a controlled wallet",
and a precise six-step payout flow: Contribution, Plan, Risk, Approval, CAW, Audit.
Dark charcoal background, lime primary accent, thin technical lines, restrained semantic colors,
high legibility at GitHub README width, no fake transaction data, no crypto coins.
```

## 2. workflow.png

- 比例：16:9
- 描述：主业务闭环与授权边界
- 重点：Risk Engine、Human Approval、CAW 三道边界

```text
16:9 architecture workflow for AgentCFO. Show six left-to-right stages:
Contribution Records, Payment Plan, Deterministic Risk Engine, Human Approval,
Cobo Agentic Wallet, Audit Report. Visually emphasize the three authorization boundaries:
Risk Engine, Human Approval, and CAW policy. Mark LLM as explanation-only.
Use flat technical UI, dark background, lime accent, no fabricated metrics or hashes.
```

## 3. architecture.png

- 比例：16:9
- 描述：Next.js、FastAPI、Planner、Risk、CAW Adapter、SQLite/Audit 的部署关系

```text
16:9 system architecture diagram for AgentCFO. Layers: Next.js frontend on Vercel,
FastAPI backend on Render, planner service, deterministic risk engine, approval gate,
CAW adapter with Mock and opt-in Real Testnet branches, SQLite audit store.
Clearly label production defaults as mock-demo and Real CAW as opt-in testnet.
Clean engineering diagram, dark neutral palette, lime accent, no unsupported cloud services.
```

## 4. tech-stack.png

- 比例：16:9
- 描述：技术栈按 frontend、backend、wallet、delivery 分组

```text
16:9 grouped technology stack graphic for AgentCFO.
Frontend: Next.js 16, React 19, TypeScript, Tailwind CSS v4.
Backend: Python, FastAPI, Pydantic, pytest, SQLite.
Wallet: Cobo Agentic Wallet SDK, Sepolia testnet.
Delivery: Vercel, Render, GitHub.
Use factual logos only when recognizable, otherwise use text labels.
```

## 5. structure.png

- 比例：4:3
- 描述：Monorepo 和 Project Init 兼容层

```text
4:3 repository structure diagram. Show product roots frontend/, app/, tests/;
governance roots docs/agents, docs/contexts, docs/outputs; asset flow inbox/ to assets/;
and compatibility links from existing docs/pm, docs/backend, frontend/docs.
Use a readable tree layout with clear canonical-versus-mapping labels.
```
