---
name: readme-polish
description: |
  项目 README 规范化打磨（结构 · 样式 · 配图 · Preview · Showcase）。
  触发：写 README / 打磨 README / 生成项目首页 / README Polish / Preview 展示 / 把 README 规范化。
  与 project-init Phase B 对齐；配图落盘 assets/images/readme/。
  含 references/ 标杆图与反推 Prompt；出图前必须读 visual-standards 与 prompts。
sync:
  global_skill: "%USERPROFILE%\\.agents\\skills\\readme-polish\\"
  synced_from_global: "2026-07-19"
  note: "仓库镜像供 review；改完回写全局"
---

# README Polish Skill

> **同步说明（review 用）**：本目录是全局 skill 镜像。改完后说一声，再写回 `%USERPROFILE%\.agents\skills\readme-polish\`。

分析项目全貌，打磨符合统一开发范式的 `README.md`：**结构、样式、配图、Preview、Showcase** 一次做完（可分步确认，但同属本 skill）。

## Skill 包结构（不只 MD）

```text
readme-polish/
├── SKILL.md
├── references/
│   ├── README.md
│   ├── visual-standards.md          # 4–6色 / 层级 / 否决项
│   ├── prompt-feed-catalog.md       # ★ Agent 直接喂：标杆清单 + Prompt 入口
│   ├── banner/ · features/ · architecture/ · tech-stack/
│   ├── workflow/ · structure/ · preview/ · showcase/
│   └── prompts/
│       ├── banner.md · features.md · architecture.md · tech-stack.md
│       ├── workflow.md · structure.md · preview-showcase.md
└── scripts/
    └── scaffold-readme-diagram-prompts.ps1
```

**Agent 出 README 配图 Prompt 前必须：**

1. Read `references/visual-standards.md` + `references/prompt-feed-catalog.md`
2. 按资产类型 Read 对应 `prompts/*.md`，并打开选定 `reference_image`
3. 反推构图，**替换为本项目真实节点**（禁止原样贴标杆）
4. 写入 `readme-image-prompts.md`：`reference_image` + Prompt + Avoid；img2img 时附标杆图
5. Preview / Showcase：`method: screenshot`；`preview/` 与 `showcase/` 只作质量条

可选脚手架（把标准与标杆拷进当前仓供用户出图）：

```powershell
powershell -File "$env:USERPROFILE\.agents\skills\readme-polish\scripts\scaffold-readme-diagram-prompts.ps1" -ProjectRoot "<绝对路径>"
```

## 触发场景

- 「帮我写 README」「打磨 README」「生成项目首页」「README Polish」「把 README 规范化」
- 「加 Preview 章节」「预览站怎么写进 README」
- project-init 进入 **Phase B · README Polish**

## 参照范文（开发范式）

按项目类型选用，**禁止照抄业务文案**，只对齐结构与信息架构意图：

| 类型 | 仓库 | 学什么 |
|---|---|---|
| 产品 Web 演示 | [xianghai-yuntu](https://github.com/Aafff623/xianghai-yuntu) | 为什么 / 功能表 / Showcase 相册 / 快速开始 / 架构分层 / 路线图 / 文档表 |
| 课程演示系统 | [ResumeWise](https://github.com/Aafff623/ResumeWise) | 边界写清、双模式、使用说明入口、ADR 链接 |
| 学习跟踪 / Bootcamp | [web3career-study-track](https://github.com/Aafff623/web3career-study-track) · [civil-service-exam-tracker](https://github.com/Aafff623/civil-service-exam-tracker) | 进度可视化、工作流、仓库结构 |
| **含金量标杆** | [agent-cfo](https://github.com/San-Y108/agent-cfo) | 黑客松级叙事密度、Highlights / Origin / 判断力、信息分层 |
| Preview 落地 | Campus Explorer：`website-preview` · `component-packs/outputs` Gallery | 本地预览站写入 README 的启动 / 浏览 / 壳图 |

## Preview vs Showcase

| | **Preview** | **Showcase** |
|---|---|---|
| **回答** | 仓库里有哪些可浏览资产？怎么本地翻一遍？ | 产品主链路长什么样？ |
| **形态** | Gallery / demo 墙 / 模板索引等可跑预览站 | `showcase-*.png` 静态相册 |
| **何时必须** | 资产库 · 多 demo · 多模板 | 有可运行产品面 |
| **何时可省略** | 单产品且无目录式预览壳 | 纯文档仓 / 尚无可截界面 |

**禁止**用 Showcase 截图冒充 Preview，或把 Preview 写成 Showcase 的别名。  
**禁止**用 Architecture / Features 说明图冒充 Showcase。

## 工作流程

### Step 0 — 确认（缺什么问什么）

1. 项目一句话定位与受众（开发者 / 评审 / 用户 / 答辩）  
2. 已有 README：保留什么、重写什么  
3. 范文偏向：产品演示向 vs 黑客松叙事向  
4. 配图：现有图路径 / 需要新出哪些契约文件名  
5. **Architecture 标杆选型**：microservices / client-server / C4 / clean-onion / aws / capability-infographic（见 `references/architecture/`）  
6. **是否需要 Preview 站**（资产库默认要；单产品可声明省略）  
7. Showcase：能否现在截图，或仅占位  

将理解结果列给用户确认后再写。

### Step 1 — 结构草稿

产出章节大纲 + 配图节点表（含 Preview / Showcase + 选用的 architecture 标杆文件名），写入：

`docs/outputs/prd/readme-diagrams/readme-diagram-brief.md`

（旧笔误 `docs/output/` 单数已废弃；一律用 `docs/outputs/`。）

### Step 2 — 配图（契约文件名 + 标杆 Prompt）

终稿目录：**`assets/images/readme/`**（禁止 `docs/images/`；禁止只丢在仓库根随意命名）。

| 文件 | 用途 | 制作与标杆 |
|---|---|---|
| `banner.png` | 页首横幅（3:1） | `banner/` + `prompts/banner.md`；宁简勿繁 |
| `features.png` | 核心功能一览 | `features/` + `prompts/features.md` |
| `architecture.png` | 系统架构 | **必选**一个 `architecture/*` + `prompts/architecture.md` |
| `tech-stack.png` | 技术栈 | `tech-stack/` + `prompts/tech-stack.md`；与 architecture 分工 |
| `workflow.png` | 用户/业务主链路 | `workflow/` + `prompts/workflow.md`；决策点明确 |
| `structure.png` | 仓库目录结构 | **优先 Markdown 树**；要画用 `structure/` |
| `preview-shell.png` | Preview 站总览 | **截图**；气质 `preview/` |
| `preview-*.png` | Preview 分区（可选 1–3） | **截图** |
| `showcase-*.png` | 产品主链路实机 | Playwright；气质 `showcase/` |

选型捷径：先打开 `references/prompt-feed-catalog.md`。

#### 2.1 产出 `readme-image-prompts.md`（执行层，关键）

路径：`docs/outputs/prd/readme-diagrams/readme-image-prompts.md`

结构要求：

- §0 全局规范：链到 skill 的 `visual-standards.md`；项目色板；命名契约；**生图系统指令**  
- 每张说明图：  
  - `asset` / 比例 / 挂载 README 章节  
  - `reference_image`（architecture/banner 必填 skill 内相对路径或已 scaffold 的 `_skill-references/...`）  
  - 结构拆解（从标杆反推的布局要点）  
  - **英文 Prompt**（已填本项目节点名）  
  - Avoid 列表  
- Showcase / Preview：写槽位与截图命令，**标明 `method: screenshot`**，不要写生图 Prompt 冒充 UI  

#### 2.2 生图模型使用方式

| 资产 | 推荐 |
|------|------|
| Banner / Architecture / Tech-stack / Features / Workflow | 用户侧 GPT Image / 同类模型；**优先 image-to-image + 标杆图**；或 Excalidraw/Figma 手绘（架构类手绘往往更稳） |
| Structure | Markdown 优先 |
| Preview / Showcase | Playwright / 实机；禁止文生图伪造产品 UI |

Agent **默认不直接调用生图 API**；负责 Prompt、标杆路径、落盘路径与 README 引用。若用户明确要求 Agent 调本地生图工具，仍必须带上 `reference_image` 与 visual-standards 约束。

### Step 3 — 组装 README

#### 3.1 产品演示向（默认 · 对齐 xianghai / ResumeWise）

推荐章节顺序：

1. **Header**：标题 · 斜体一句话 · Banner · shields 徽章 · 锚点导航（为什么 · 功能 · **Preview** · 演示 · 快速开始 · 架构 · …）  
2. **为什么需要** — 痛点 3 条内 + 主线收敛表  
3. **功能** — `features.png` + 功能表；写清 Wave / MVP **边界**  
4. **Preview** — 见 Step 5（资产库 / 多 demo **应当有**；单产品可省略并声明）  
5. **演示 / Showcase** — 推荐路径 + 截图表（或占位）+ 可选页面清单  
6. **快速开始** — 可复制命令；登录演示账号若有则写明  
7. **架构** — `architecture.png` + 分层表；`tech-stack.png`  
8. **用户主链路** — `workflow.png` + 实现要点  
9. **目录结构** — `structure.png` 或折叠目录树  
10. **路线图** — 状态表  
11. **文档** — 链到 CONTEXT / ADR / AGENTS / assets README  
12. **License / 说明**

#### 3.2 黑客松 / 叙事向（对齐 agent-cfo · study-track）

可用英文锚点章节（按需裁剪）：

`✨ Highlights` · `🌱 Origin` · `📊 Progress` · `📂 Repo-Structure` · `⚙️ Workflow` · `💡 Judge` · `🏆 Hackathon` · `🔗 Link` · `🔒 Privacy`

若有 Preview 站，在 Highlights 或单独 `🖥️ Preview` 中写启动与壳图。

标题格式：`## emoji English-Name (中文名)`（过长英文可用中文例外）。

### Step 4 — 样式规范

- **中英混排**：术语保留英文（`Agent`、`MVP`、`ADR`、`Preview`），叙事用中文  
- **重点**：`**粗体**` = 结论；`` `路径/命令` `` = 可复制项  
- **表格**：功能 / 进度 / 文档 / Preview 覆盖 / Showcase 优先用表  
- **折叠**：长目录、旧截图用 `<details>`  
- **徽章**：`for-the-badge`；绿=完成、橙=进行、灰=未开始  
- **最多三级标题**；导航后可用 `---`，章节间少加无意义分割线  
- **语气**：有观点、有节制、有结构；Origin 可有个人叙事但不煽情  
- **可验证**：进度与链接必须真实，禁止编造星标/截图

### Step 5 — Preview（README 模块）

资产库 / HTML demo 墙 / 多模板包：**必须**有独立 `#preview` 小节。

```markdown
## Preview

一句话：本仓用本地预览站浏览全部 [组件/演示/模板]，不是业务产品站。

### 启动

```bash
cd <preview-root>
npm install   # 若需要
npm run dev   # 或 python -m http.server …
```

默认打开：`http://127.0.0.1:<port>/…`

### 怎么浏览

1. …
2. …

### 预览壳

![Preview shell](assets/images/readme/preview-shell.png)

### 覆盖范围

| 分区 | 数量 | 说明 |
|---|:---:|---|
| … | … | … |
```

- Preview 源码在产品层（如 `src/website-preview/`、`src/.../outputs/`），不进 `docs/`  
- Init 可占位：启动命令 + 覆盖表 +「壳图待补」  
- 单产品无预览壳：在 README 或 brief 写明「本仓无 Preview 站，仅用 Showcase」

### Step 6 — Showcase

**可占位（init）**

```markdown
### 推荐演示路径
（文字步骤）

### Showcase
> 真机截图待功能与视觉验收后补充。槽位：Landing / 首页 / 详情 / …
```

**可实装**

1. 本地静态服务或 `npm run dev` 跑通主链路  
2. Playwright 按槽位截图 → `assets/images/readme/showcase-*.png`  
3. README 用相对路径引用；删除空头占位句  

截图质量对齐 `references/showcase/`：颜色统一、信息密度高、无多余装饰、真实运行状态。

## 输出落盘

```text
project-root/
├── README.md
├── assets/images/readme/
│   ├── banner.png
│   ├── features.png · architecture.png · tech-stack.png
│   ├── workflow.png · structure.png
│   ├── preview-shell.png · preview-*.png
│   └── showcase-*.png
└── docs/outputs/prd/readme-diagrams/
    ├── readme-diagram-brief.md
    ├── readme-image-prompts.md      # 含 reference_image + 反推 Prompt
    ├── visual-standards.md          # 可选：从 skill scaffold
    └── _skill-references/architecture/  # 可选：标杆副本，仅供生图参考
```

## 约束

- 不替用户做最终审美拍板——Banner / 主色 / architecture 标杆选型须确认  
- 不过度设计——章节按需，不硬塞满模板  
- 已有 README **优先迭代**，避免无必要从零重写  
- 不与 `CONTEXT.md` / `LANGUAGES.md` 抢唯一事实源  
- Agent 默认不直接调用生图模型；只提供 **标杆 + 反推 Prompt + 目录契约**  
- 配图路径以 **`assets/images/readme/`** 为准（旧 skill 中的 `assets/banner.png` 根路径已废弃）  
- Preview 与 Showcase **分文件名、分章节**，禁止混用  
- **禁止**把 `references/` 里第三方标杆图原样当作本项目 README 配图发布  
- 颜色 ≤ 5；架构图禁止蜘蛛网；Structure 优先代码块树  
