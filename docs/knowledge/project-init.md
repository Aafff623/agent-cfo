---
name: project-init
description: 接手 / 新建仓库的体系化初始化。仓内 review 副本；执行以全局 skill 为准。
sync:
  global_skill: "%USERPROFILE%\\.agents\\skills\\project-init\\SKILL.md"
  direction: "全局 skill → 本文件覆盖同步；改规范优先改全局"
  synced_at: "2026-08-08"
---

> **同步说明**：正文与全局 `project-init` skill §0–8 对齐（2026-08-08）。Agent 执行以 `%USERPROFILE%\\.agents\\skills\\project-init\\SKILL.md` 为准。
# project-init — 接手 / 新建仓库的体系化初始化

> **用途**：无论从零开仓，还是接手客户/同学的现有仓库，先完成本文件规定的初始化，再进入业务 theme。  
> **性质**：可迁移操作规范（knowledge），不是某个产品的 PRD。  
> **演进说明**：吸收 Campus Explorer 落地经验：媒体进 **`assets/`**；根 **`LANGUAGES.md`**；流程目录 **`outputs/{prd,report,handoff,commit-history}/`**；去掉与根文件重复的 agents 冗余件。  
> **任务流细则**：目标仓 `docs/agents/workflow.md` · 根 `AGENTS.md`  
> **README 打磨**：全局 skill **`readme-polish`**（结构 · 样式 · 配图 · **Preview** · Showcase）

---

## 0. 适用范围与目标

| 场景 | 是否跑 project-init |
|---|---|
| 新接单、仓库尚无 Agent 资产 | **必须**（Full 模式） |
| 自己从零开项目 | **必须**（Full 模式） |
| 老项目 / 资产维护不到位，需修复迁移 | **必须**（Full 模式，含 Agent 并行调研） |
| 已规范仓库上开业务功能 | 不必重复；只跑业务 PRD/handoff |
| 仅改一行文案 | 不必 |
| 只同步 Cursor rules | **Minimal 模式**（仅 Step 0） |
| 已有业务仓，补规则/目录骨架 | **Lite 模式**（Step 0 + 补缺目录） |

**完成定义（Definition of Done）**

1. 根入口与 `docs/` + `assets/` 骨架就位；Issue tracker / triage / domain 已写入且可被 Matt Pocock 系 skill 消费。  
2. 根 `README.md` 经 **README Polish** 达到可对外展示的结构、样式与视觉基线（配图 / **Preview** / Showcase 可先占位后补齐）。  
3. 后续业务开发可直接走：`Issue → PRD → handoff → Review → commit-history`，无需再争论「文件放哪」。
4. **Full 模式（老项目）**：Agent 并行调研完成，`CONTEXT.md` 已填充项目分析结果。

**单一事实源原则**

| 事实类型 | 唯一入口 |
|---|---|
| 领域术语与硬约束 | 根 `CONTEXT.md`（多端则 + `CONTEXT-MAP` / `docs/contexts/*`） |
| 共享用词（Agent 输出必须用的词） | 根 `LANGUAGES.md` |
| Agent 硬约束 / 任务流门禁 | 根 `AGENTS.md` |
| 人读摘要与运行说明 | 根 `README.md` |

禁止同一事实在多处各写一版且互相漂移。  
**禁止**再维护 `docs/agents/language.md` / `docs/agents/context.md`（与根 `LANGUAGES.md` / `CONTEXT.md` 重复）。

---

## 0.5 输出格式（强制 · 与用户级规范对齐）

执行本 skill 的**所有汇报**（需求对齐、阶段停点、验收、进度说明）必须符合用户级输出规范。真相源：`~/.claude/CLAUDE.md` / `%USERPROFILE%\.cursor\AGENTS.md` / `answer-format.mdc`（humanizer-tta Voice Layer）；以下为执行层要点：

| 规范 | 执行要求 |
|---|---|
| 语言（§0.1） | 简体中文；代码 / 路径 / 命令 / 术语保留原文 |
| 轮末总结（§0.4） | 每轮末尾附两列表格：`本轮做了什么 / 刚又完成`（1–3 句，动词开头）；表格下方补一句感想小心思 |
| 阶段汇报（Dual-Track） | 结论先行 + 过程证据；证据以表格 / 白话步骤为主，禁长段散文 |
| 表情（§15） | 全程融入 emoji+颜文字组合（如 ☕(￣▽￣)ノ）；代码块内不放；用户着急时收敛 |
| 称呼与禁语 | 用户称「小 A」；禁客服套话（好的我来帮您…）、禁 em dash / en dash |
| 图示（§16） | IDE 用白话 Mermaid；CLI 用白话步骤 1→2→3 |
| Gate 停点 | 每阶段说明：做了什么、改了哪些路径、你（用户）怎么 Review |

---

## 1. 阶段总览

```text
Phase A          资产初始化 + 外部资产融合 + 需求对齐确认
    ↓
Phase B          README Polish（结构 · 样式 · 配图 · Preview · Showcase）
    ↓
Gate             你 Review 本轮 init 产物 → 再开第一个业务 theme
```

两阶段可在同一会话内连续做，但 **Gate 前不开启大规模业务编码**（与 `AGENTS.md` PRD 门禁一致）。

| Phase | 一句话 |
|---|---|
| **A · 资产** | 骨架落盘；外来包/图/文按规范归位；与用户确认需求与目录决策 |
| **B · README Polish** | 用 `readme-polish` 打磨 README：章节结构、版式、配图契约、**Preview 展示**与 Showcase（可占位） |

---

## 2. Phase A — 资产初始化 · 融合 · 需求对齐

### 2.1 Cursor MDC Rules（强制，新项目与存量补骨架都要做）

> 全局用户规则是**真相源**；每个项目必须在仓库内落盘一份，保证本仓 Agent 始终加载，不依赖「碰巧开着全局 rules」。

**真相源（用户级，只读拷贝，勿改内容语义）：**

| 文件 | 作用 |
|------|------|
| `%USERPROFILE%\.cursor\rules\windows-path-discipline.mdc` | Windows 路径：反斜杠、MINGW 转换、ENOENT 处理 |
| `%USERPROFILE%\.cursor\rules\windows-shell-discipline.mdc` | Windows Shell：路径 quoting、`nul` 重定向 |
| `%USERPROFILE%\.cursor\rules\answer-format.mdc` | Dual-Track 回答格式；白话 Mermaid（跨项目，与用户级 `AGENTS.md` §16 对齐） |
| `%USERPROFILE%\.cursor\rules\AGENTS.mdc` | 全局 Agent 规范镜像（语言/双轨/编码纪律/`Mermaid Diagram Style`）；真相源为 `%USERPROFILE%\.cursor\AGENTS.md` |
| `%USERPROFILE%\.cursor\rules\commit-history.mdc` | commit-history 维护：表格格式、分支组织、归档策略 |

**项目落盘目标（必须写入当前仓库）：**

```
.cursor/
└── rules/
    ├── windows-path-discipline.mdc   # alwaysApply: true
    ├── windows-shell-discipline.mdc  # alwaysApply: true
    ├── answer-format.mdc             # alwaysApply: true（含白话 Mermaid）
    ├── AGENTS.mdc                    # alwaysApply: true（与用户级 AGENTS.md 同步）
    └── commit-history.mdc            # alwaysApply: true
```

**执行要求：**

1. 解析用户目录：PowerShell 用 `$env:USERPROFILE`；写 `file_path` 时用已解析的绝对 Windows 路径（反斜杠），禁止把 `%USERPROFILE%` / `$HOME` 原样塞进工具参数。
2. 若项目 `.cursor\rules\` 不存在 → 创建。
3. 从用户级目录**复制**上述五个 `.mdc` 到项目 `.cursor/rules/`（逐份按内容比对：与用户级源文件完全一致则跳过；缺失或内容不一致则覆盖同步——只判断一致与否，不判断新旧）。**禁止**在项目里手改这些文件的语义；要改只改用户级真相源，再靠本 Step 覆盖同步。
4. 保持 frontmatter：`alwaysApply: true`；不要删改纪律正文。
5. 同步前确认用户级 `AGENTS.md` 与 `AGENTS.mdc`、以及 `answer-format.mdc` 中的 Mermaid/输出风格条款已是最新（以 `%USERPROFILE%\.cursor\AGENTS.md` 为准）。
6. 在 `AGENTS.md` / `CLAUDE.md`（若本 Phase 会写）中声明项目规则资产。
7. **存量业务项目**走 Lite 模式时：本 Step 仍**不可跳过**；其余步骤按 Lite 范围执行。

### 2.2 与用户对齐（写盘前必做）

**A. 静默套用全局默认（不重复问）**

| # | 确认项 | 默认值 |
|---|--------|--------|
| 1 | Issue tracker | 本地 `.scratch/<feature>/` markdown |
| 2 | Triage 标签词汇 | 五种 canonical 标签（needs-triage / needs-info / ready-for-agent / ready-for-human / wontfix） |
| 3 | 单/多 CONTEXT | 单文档：`CONTEXT.md` + `docs/adr/` |
| 4 | Cursor MDC rules 同步 | 必须同步（§2.1 已强制执行，此处不重复问） |

直接应用以上默认，回复里报一句"按全局默认使用 xxx"；仅当仓库有明显特殊信号才就对应单项向用户确认。

**B. 必须真人拍板的开放项（用 `AskUserQuestion` 批量问，1–2 批问完）**

| # | 确认项 | 说明 | 默认值（可一键跳过） |
|---|--------|------|---------------------|
| 1 | 外部资产清单 | zip、旧 docs/images、原型图…从哪来、迁到哪 | 无外部资产 |
| 2 | 产品层根 | `src/` / `frontend/` / monorepo 边界 | `src/` |
| 3 | 首个业务 theme 名 | 未定则 Phase A 只做骨架 | 只做骨架 |
| 4 | 项目预期 | 规模/受众/核心产物 | 内部工具 |
| 5 | Handoff 形式 | 启用 A–E 哪些场景 | 默认只 A |
| 6 | 输出语气 + 回答格式 | 是否建 `docs/agents/voice.md` | 默认建 |

Lite 模式跳过整个 B 组，只走 A 组默认。Full 模式支持「全部默认」一键跳过。

### 2.3 必用 Skill / 命令

| 顺序 | Skill / 动作 | 作用 |
|---:|---|---|
| 0 | **Cursor MDC Rules（§2.1）** | 从用户级同步 `windows-path-discipline.mdc` + `windows-shell-discipline.mdc` + `answer-format.mdc` + `AGENTS.mdc` + `commit-history.mdc` 到项目 `.cursor/rules/` |
| 1 | **`setup-matt-pocock-skills`** | 探查仓库 → 写入 `issue-tracker.md`、`triage-labels.md`、`domain.md`；在 `AGENTS.md` / `CLAUDE.md` 挂 `## Agent skills` |
| 2 | 对齐 **`docs/agents/`** 流程件 | **仅**：`workflow.md`、`deliver.md`、`archive.md`、`domain.md`、`issue-tracker.md`、`triage-labels.md` |
| 3 | 写入根入口 | `AGENTS.md`、`CLAUDE.md`、`CONTEXT.md`、`LANGUAGES.md`、`CONTEXT-MAP.md`（多端）、`README.md` 初稿 |
| 4 | **引用 `humanizer-tta` skill** | 在 `AGENTS.md` / `CLAUDE.md` 顶部写入输出语气引用（见 §2.9）；若项目用 opencode，可选复制 SKILL.md 到 `.opencode/skills/` |
| 5 | 骨架目录 | 见 §2.6 `docs/`、§2.7 `assets/` |
| 6 | **外部资产融合** | 见 §2.4 |
| 7 | **Agent 并行调研**（Full 模式，老项目） | 见 §2.4.1 |
| 8 | （可选）**`to-issues`** / **`to-prd`** / **`triage`** | 首个业务 theme 已定时再用 |

### 2.4 外部资产融合

若接手仓或本地已有散落资产，按表归位（先列迁移清单给用户确认）：

| 来源 | 归入 |
|---|---|
| 上游 zip / 原版源码包 | `assets/backup/` |
| 旧 `docs/images/readme/` 或随意 `assets/*.png` | `assets/images/readme/`（改 README 引用） |
| 品牌 Logo / 头像槽 | `assets/images/icon/` · `assets/images/avatar/`（或产品约定的 `assets/brand/`，须写入 `assets/README.md`） |
| 演示视频 | `assets/video/` |
| 已有可跑产品代码 | 对应产品目录（如 `src/` / `frontend/`），**不**塞进 docs |

融合原则：backup 只读；工作副本可编辑；路径写进 `assets/README.md` 与 CONTEXT（必要时）。

### 2.4.1 Agent 并行调研（Full 模式，老项目专用）

> 针对老项目或资产维护不到位的项目，在 Phase A 早期启动 Agent 并行调研，将分析结果填充到 `CONTEXT.md`。

**触发条件**：Full 模式，且检测到项目已有部分资产但结构/内容不符合最新规范。

**并行调研维度**（5 个 Agent 并行）：

| Agent | 调研维度 | 输出 |
|---|---|---|
| Agent 1 | 项目结构分析 | 目录树、关键文件识别、入口文件 |
| Agent 2 | 技术栈识别 | 框架、依赖、构建工具、包管理 |
| Agent 3 | 资产现状评估 | 现有 docs/assets/ 完整性、缺口清单 |
| Agent 4 | 业务领域分析 | 核心功能、用户流程、领域术语 |
| Agent 5 | 规范差距分析 | 与最新规范的差距清单、修复建议 |

**填充目标**：

| 资产文件 | 填充内容 | 更新方式 |
|---|---|---|
| `CONTEXT.md` | 项目定位、技术栈、业务领域、术语 | 覆盖式（保持单一事实源） |
| `LANGUAGES.md` | 共享用词、Issue 规范、任务流词汇 | 覆盖式 |
| `AGENTS.md` | 硬约束、任务流摘要、Review 门禁 | 覆盖式 |
| `docs/outputs/report/{theme}/` | 调研分析报告（可选） | 新建 |

**执行规则**：
- 已有 `CONTEXT.md` 时先备份（`.scratch/context-backup-YYYYMMDD.md`）再覆盖
- 分析结果必须基于实际代码和文件，禁止臆测
- 不确定的术语标注 `【待确认】`，由用户后续拍板

### 2.5 根目录职责（L0）

| 文件 | 职责 | 反模式 |
|---|---|---|
| `AGENTS.md` | 跨工具硬约束、路径表、任务流摘要、Review 门禁 | 产品说明书 |
| `CLAUDE.md` | 维护协议、三层加载、偏好归档 | 与 AGENTS 大段矛盾重复 |
| `CONTEXT.md` | 领域术语、硬约束、技术栈事实 | 临时笔记、未裁定猜测 |
| `LANGUAGES.md` | 共享词汇入口（Issue / 任务流 / 领域用词） | 与 CONTEXT 冲突的第二套定义 |
| `CONTEXT-MAP.md` | 多上下文索引 | 单端空壳 |
| `README.md` | 人类入口（Phase B 打磨） | 充当 Issue / 术语真相源 |

### 2.6 `docs/` 目标树

```text
docs/
├── README.md
├── agents/              # workflow · deliver · archive · domain
│                        # · issue-tracker · triage-labels
│                        # · voice（输出语气，可选）
│                        # （不要 language.md / context.md）
├── adr/                 # 000N-kebab-title.md
├── contexts/            # 可选：{weapp,admin,api}/CONTEXT.md
├── knowledge/           # 可迁移知识（可放本文件副本）
├── glossary/            # 人 ⇄ Agent 认知对齐术语库（如 frontend-ui.md）
└── outputs/             # 任务产物（按需建子目录, 不预铺空壳）
    ├── report/{theme}/        # 调研分析报告（与 PRD 分离）
    ├── prd/{theme}/           # PRD（产品需求文档）
    ├── handoff/{theme}/       # 任务交接快照（覆盖式更新）
    └── commit-history/        # commit 攒批记录（按分支组织）
        ├── {branch}/
        │   └── YYYY-MM-DD.md
        └── archive/           # 已合并分支归档
```

> `outputs/{report,prd,handoff,commit-history}` 在**有对应产物时才建**；不要为「凑齐四类」预建空目录或 `.gitkeep`。

业务流程对齐：

```text
Issue（GitHub 或 Local Markdown）
  → docs/outputs/report/{theme}/        # 调研分析（可选，先于 PRD）
  → docs/outputs/prd/{theme}/prd.md     # PRD（需求）
  → 拆解 To-Do / 子任务
  → docs/outputs/handoff/{theme}/YYYY-MM-DD-{branch}-{task}.md
  → 实施 → Review → archive
```

### 2.7 `assets/` 目标树

> **按需创建**：下表是**完整形态**，不是强制铺满。只建真正要用的子目录；长期空着的槽位（`avatar/` `icon/` `video/` `ppt/` `speeches/`）**不要**用 `.gitkeep` 占位——用到时再建。轻量主题通常只需 `images/readme/`。

```text
assets/                       # 按需：缺省只需 README.md + images/readme/
├── README.md
├── backup/                    # 上游 zip / 原版只读备份（有才建）
├── images/
│   ├── readme/                # README 配图 + Showcase（默认需要）
│   ├── avatar/                # 按需
│   └── icon/                  # 按需
├── video/                     # 按需
├── ppt/                       # 演示文稿（PPT / Keynote 源文件）
└── speeches/                  # 演讲稿 / 逐字稿
```

| 路径 | 职责 | 何时建 |
|---|---|---|
| `assets/backup/` | 只读收录；日常编辑改产品目录 | 有上游原版要留底时 |
| `assets/images/readme/` | banner / architecture / features / tech-stack / workflow / structure / **preview-*** / showcase-* | 默认 |
| `assets/images/avatar/` · `icon/` | 文档或演示槽位（业务 `public/` 仍归应用自身） | 有实际图时 |
| `assets/video/` | 演示视频 | 有视频时 |
| `assets/ppt/` | 演示文稿源文件（PPT / Keynote） | 做演示时 |
| `assets/speeches/` | 演讲稿 / 逐字稿 / 项目介绍稿 | 有稿件时 |
| `assets/README.md` | 媒体约定与还原说明 | 默认 |

**禁止**新建 `docs/images/`；**禁止**为「凑齐骨架」给空目录加 `.gitkeep`。

### 2.8 Phase A 验收

- [ ] `.cursor/rules/windows-path-discipline.mdc` 已落盘且 `alwaysApply: true`
- [ ] `.cursor/rules/windows-shell-discipline.mdc` 已落盘且 `alwaysApply: true`
- [ ] `.cursor/rules/answer-format.mdc` 已落盘且 `alwaysApply: true`（含白话 Mermaid，与用户级 `AGENTS.md` §16 一致）
- [ ] `.cursor/rules/AGENTS.mdc` 已落盘且 `alwaysApply: true`（与 `%USERPROFILE%\.cursor\AGENTS.md` / `AGENTS.mdc` 内容一致）
- [ ] `.cursor/rules/commit-history.mdc` 已落盘且 `alwaysApply: true`
- [ ] 与用户的关键确认项已对齐（§2.2）
- [ ] `setup-matt-pocock-skills` 决策已落盘；`## Agent skills` 路径真实
- [ ] 根：`AGENTS` / `CLAUDE` / `CONTEXT` / `LANGUAGES` /（`CONTEXT-MAP`）；AGENTS/CLAUDE 已引用 `humanizer-tta` skill + Windows Rules + Answer Format
- [ ] `docs/agents` **无** `language.md`、`context.md`
- [ ] `docs/outputs/{report,prd,handoff,commit-history}` · `adr` · `knowledge` · `glossary`
- [ ] 若 B组#6 启用：`docs/agents/voice.md` 已产出，且含「回答格式」并链到 `answer-format.mdc`
- [ ] `assets/` + `assets/README.md`；外部资产已融合或迁移清单已关闭
- [ ] ADR-0000（或等价）已说明采用 ADR
- [ ] 无密钥入库；无本机绝对路径作唯一说明
- [ ] **Full 模式（老项目）**：Agent 并行调研完成，`CONTEXT.md` 已填充项目分析结果（§2.4.1）

---

### 2.9 Humanizer Skill 安装

> 确保项目 Agent 默认使用 `humanizer-tta` 语气人格（Personal Hermes Engineer，非 AI 腔；已取代旧 `humanizer-output-style`）。真源：`~/.agents/skills/humanizer-tta/SKILL.md`，镜像于 `~/.config/opencode/skills/` · `~/.cursor/skills/`。两种方案：

| 方案 | 做法 | 适用 |
|------|------|------|
| **A · 引用全局** | 在项目 `AGENTS.md` / `CLAUDE.md` 顶部写 `> **Output Style**: humanizer-tta skill → ~/.agents/skills/humanizer-tta/SKILL.md` | 单人单机，无需独立维护 |
| **B · 复制到项目** | 复制 SKILL.md 到 `.opencode/skills/humanizer-tta/SKILL.md` | 团队共用，或需独立调整语气 |

**AGENTS.md 引用模板**（方案 A）：

```markdown
# AGENTS.md

> **Output Style**: `humanizer-tta` skill — 常驻语气人格（Hermes 工程师口吻）+ 成稿去 AI 味。加载路径：`~/.agents/skills/humanizer-tta/SKILL.md`
```

**CLAUDE.md 引用模板**（方案 A）：

```markdown
# CLAUDE.md

> **Output Style**: `humanizer-tta` — see `~/.agents/skills/humanizer-tta/SKILL.md`
```

若项目选了方案 B，Agent 复制后需用 `read` 验证复制件中文可读。

---

> 结构、样式、图片、配图、**Preview**、Showcase **同属本 Phase**。  
> 执行时加载全局 skill：**`readme-polish`**。

### 3.1 必用 Skill 与参照范文

| 项 | 值 |
|---|---|
| Skill | **`readme-polish`** |
| 产品向范文 | [xianghai-yuntu](https://github.com/Aafff623/xianghai-yuntu) · [ResumeWise](https://github.com/Aafff623/ResumeWise) · [civil-service-exam-tracker](https://github.com/Aafff623/civil-service-exam-tracker) · [web3career-study-track](https://github.com/Aafff623/web3career-study-track) |
| 含金量标杆 | [agent-cfo](https://github.com/San-Y108/agent-cfo)（黑客松 README 范式） |
| Preview 落地参照 | Campus Explorer：`website-preview`（静态演示墙）· `component-packs/outputs`（组件 Gallery） |
| 配图 brief（契约层） | `docs/outputs/prd/readme-diagrams/readme-diagram-brief.md`：章节地图 + 资产清单 + 设计语言 + 验收（注意是 **outputs** 复数；旧写作 `docs/output/` 视为笔误） |
| 出图 prompt（执行层） | `docs/outputs/prd/readme-diagrams/readme-image-prompts.md`：每张图详细 prompt，投喂 GPT image-to-image |
| 终稿图目录 | **`assets/images/readme/`** |

### 3.2 README Polish 覆盖范围

| 维度 | 做什么 |
|---|---|
| **结构** | Header（标题 · 一句话 · Banner · 徽章 · 锚点导航）+ 为什么 / 功能 / **Preview** / 演示·Showcase / 快速开始 / 架构 / 主链路 / 目录 / 路线图 / 文档 |
| **样式** | 中英混排、表格密度、徽章语义色、导航锚点；不过度装饰。**目录结构 / 仓库树 / 结构摘要 / Key docs 必须直接呈现**，禁止 `<details>` 折叠（细则见 `readme-polish` Step 4；仅非结构附录可折叠） |
| **配图** | §3.3 文件名契约；GPT Image 出图由用户执行，Agent 写 brief + Prompt |
| **Preview** | 可本地打开的预览站：入口路径 · 启动命令 · URL · 怎么浏览 · 预览壳截图（见 §3.5） |
| **Showcase** | 产品主链路推荐路径 + 真机界面相册；init 可占位，功能就绪后用 Playwright 替换（见 §3.6） |

### 3.3 标准配图清单（文件名即契约）

| 文件 | 用途 |
|---|---|
| `banner.png` | 页首横幅（建议 3:1） |
| `features.png` | 核心功能一览 |
| `architecture.png` | 系统架构 |
| `tech-stack.png` | 技术栈分层 |
| `workflow.png` | 用户/业务主链路 |
| `structure.png` | 仓库目录结构 |
| `preview-shell.png` | **Preview 站总览**（画廊壳 / 卡片墙 / 侧栏选分区） |
| `preview-*.png` | Preview 代表性分区或条目缩略（可选） |
| `showcase-*.png` | 产品主链路实机界面相册（Playwright） |

引用示例：`assets/images/readme/banner.png` · `assets/images/readme/preview-shell.png`。

### 3.4 Preview 与 Showcase 分工（必读）

| | **Preview** | **Showcase** |
|---|---|---|
| **回答的问题** | 「仓库里有哪些可浏览资产？怎么本地翻一遍？」 | 「产品主链路长什么样？」 |
| **典型对象** | 组件包 Gallery、HTML demo 墙、模板缩略索引、Storybook 类壳 | Landing / 登录 / 核心流程页 |
| **交互** | 本地可跑、可切换分区/条目 | 静态截图举证（可附演示路径文字） |
| **README 重点** | 启动命令 · 入口 URL · 浏览方式 · `preview-*.png` | 推荐路径 · `showcase-*.png` |
| **何时必须** | 资产库 / 多 demo / 多模板主题 **应当有** | 有可运行产品面时 **应当有** |
| **何时可省略** | 单产品应用且无「目录式预览壳」 | 纯文档仓或尚无可截界面 |

二者可同时出现，**不要互相替代**：Preview 不是 Showcase 的别名。

### 3.5 Preview 展示设计（README 模块）

#### 何时建 Preview 站

| 仓类型 | Preview 期望 |
|---|---|
| 组件 / 区块资产库 | Gallery：侧栏分区 + 变体切换 + 实时渲染（或等价） |
| HTML / 静态 demo 集合 | 统一预览站（卡片墙 + iframe / 链接打开） |
| 多套独立模板包 | 模板索引页（缩略图 + 进入各模板 `dev` 的说明） |
| 单产品 Web 应用 | 通常 **不**单独建 Preview 站；用 Showcase 即可 |

Preview 源码落在产品层（如 `src/website-preview/`、`src/.../outputs/`），**不要**塞进 `docs/`。路径与启动方式写入 `CONTEXT.md` / `LANGUAGES.md`（领域词）与 README。

**实现层对齐（跨主题）**：Workbench 内探索层 Preview / `src/` 目录以 Motionsites 为标杆——轻量静态壳、全宽全貌、源码包装 ZIP、禁止为验收批量起 Next。完整踩坑、流程与可粘贴 Agent Prompt → [`ui/motionsites-preview-align.md`](./ui/motionsites-preview-align.md)。

#### README 中的 Preview 章节模板

锚点建议：`#preview`（导航里与「演示 / Showcase」分开）。

```markdown
## Preview

一句话：本仓用本地预览站浏览全部 [组件/演示/模板]，不是业务产品站。

### 启动

`cd` 到预览根 → 安装（若需要）→ 启动命令 → 默认 URL（如 `http://127.0.0.1:8765/...`）。

### 怎么浏览

1. 侧栏 / 卡片选分区（或 Category）
2. 切换变体 / 打开条目
3. （可选）交互门槛：点击启用 iframe、Light/Dark 等

### 预览壳

![Preview shell](assets/images/readme/preview-shell.png)

### 覆盖范围

| 分区 / Category | 数量 | 说明 |
|---|:---:|---|
| … | … | 链到 `ASSETS.md` 或 registry 亦可 |

> Init 阶段可先写启动命令 + 覆盖表，图用占位说明「Preview 壳截图待补」。
```

#### Preview 配图约定

1. **`preview-shell.png`**：整页预览站一帧（含导航结构，证明「能翻」）。  
2. **`preview-*.png`**（可选）：1–3 张代表性分区，避免把 README 做成整库相册。  
3. 截图工具：Playwright 对 **Preview 站本身** 截图；与产品 Showcase 分文件名，禁止混用 `showcase-*` 冒充 Preview。  
4. 若 Preview 尚未落地：README 写清「计划路径 + 启动占位」，并在 Phase B 验收中标明待续作。

#### Preview 验收口径

- [ ] README 有独立 **Preview** 小节（或已书面说明「本仓无 Preview 站、仅用 Showcase」）  
- [ ] 启动命令与 URL 可复制；工作目录真实  
- [ ] 浏览方式 1–3 条；覆盖范围可核对  
- [ ] `preview-shell.png` 已引用或已占位说明  

### 3.5.1 README 本地预览壳（`preview-readme.{html,css,js}`）

> **是什么**：主题/仓库根的一套纯静态壳，本地 HTTP 打开即把 `README.md` 按 GFM 渲染出来。边写边看排版，改完点「重新加载」，**不必 commit / 推远端才看到效果**。走 README Polish 的仓库默认生成。

#### 三文件职责

| 文件 | 职责 |
|---|---|
| `preview-readme.html` | 结构 + 内联 `window.__PREVIEW_README__` 配置（语言 / 标题 / 提示 / 端口错误文案 / 页脚）；引 CDN `github-markdown-css` + `marked` |
| `preview-readme.js` | `fetch('./README.md')` → `marked.parse` → 注入；`file://` 保护 + 「重新加载」按钮 + 加载状态 |
| `preview-readme.css` | 工具栏 / 页宽 / 状态条样式 |

#### 与邻居的区别（勿混）

| 产物 | 回答 | 形态 |
|---|---|---|
| `preview-readme.html` | 「README 本身渲染出来长什么样？」 | 渲染 `README.md` 的壳 |
| `src/website-preview/`（Preview 站） | 「仓库有哪些资产、怎么本地翻？」 | 资产 Gallery |
| `preview-shell.png` | Gallery 总览截图 | 静态图（进 README） |

三者**不互相替代**：README 壳不是 Gallery，Gallery 截图不是 README 壳。

#### 约定

- **端口**（仅当目标仓维护 `port-registry` 时）：取 registry「README preview shell」段（如 `8090–8099`），每主题唯一，写进主题 `CLAUDE.md` 与 registry。无 registry 的仓可声明省略预览壳（见 Firefly `CLAUDE.md`）。
- **启动**：主题根执行 `python -m http.server <port>`，访问 `http://127.0.0.1:<port>/preview-readme.html`。
- **必须 HTTP 打开**：`file://` 无法 `fetch` README，壳会给出提示；错误文案里的端口须与实际一致。
- **配置本地化**：`window.__PREVIEW_README__` 的标题 / 提示 / 页脚随主题改；页脚指向预览站与 `assets/images/readme/`。

#### 何时建 / 何时省

| 场景 | README 壳 |
|---|---|
| 走 README Polish 的资产库 / 模板 / 多 demo 主题 | **默认建** |
| 纯后端 / 无 README 展示需求 | 可省 |

#### 反模式

- ❌ 直接 `file://` 双击打开（`fetch` 失败，白屏）
- ❌ 端口硬编码、与 `port-registry` 撞车或不回写
- ❌ 把 README 壳当资产 Gallery，或用 Gallery 顶替 README 壳

### 3.6 Showcase（本 Phase 内完成口径）

**Init 时（可占位）**

1. 写清推荐演示路径。  
2. 标明「真机截图待视觉验收后补充」。  
3. 用表格 / HTML 注释预留槽位。

**功能就绪后（仍算 README Polish 续作，不必重开 init）**

1. 本地跑通主链路。  
2. Playwright 截图 → `assets/images/readme/showcase-*.png`。  
3. 更新 README 引用，收窄占位文案。

### 3.7 执行步骤（与 readme-polish 对齐）

1. **读仓 + 确认**：定位、栈、受众、已有 README 优劣；是否需要 Preview 站 → 向用户确认。  
2. **对标范文**：按项目类型选「产品演示向」或「黑客松叙事向」，**禁止照抄他仓业务文案**。  
3. **结构草稿 → brief（契约层）**：列章节与配图节点（含 Preview / Showcase）→ `readme-diagram-brief.md`（章节地图 + 资产清单 + 设计语言 + 验收）。  
4. **出图规范 MD（执行层，关键产物）**：Agent 结合**项目实际 + 主题色 + 主题元素**，为每张契约图产出详细出图说明 → `readme-image-prompts.md`：
   - §0 全局规范：项目定位 · 视觉总调（色板 / 材质 / 光影）· 出图优先级 · 命名契约 · **给 GPT 的系统指令模板**（可粘贴到对话开头）；
   - 每张图：基本信息 · 一句话描述 · 详细描述 · 参照信息 · 元素清单 · 构图建议 · **英文 Prompt（直接喂 GPT image-to-image）** · 中文补充提示。
   - 范例：本仓 `readme-image-prompts.md`。  
5. **出图**：用户把 `readme-image-prompts.md` 投给 GPT image-to-image 生成图 → 落盘 `assets/images/readme/`。**Agent 不直接生图**（多数模型无能力），只产出可投喂的规范 MD。  
6. **组装 README**：结构 + 样式 + 图引用 + **Preview 模块** + Showcase（占位或实图）。  
7. **用户 Review** 文案、图、路径是否与 CONTEXT / LANGUAGES 一致。

### 3.8 Phase B 验收

- [ ] README 章节完整、扫读友好，与范文意图对齐（非照抄）  
- [ ] 配图契约文件名与引用一致（缺失项已占位说明）  
- [ ] **出图规范 MD**（`readme-image-prompts.md`）已产出：全局规范 + 每张图 prompt（可投喂 GPT image-to-image）  
- [ ] **Preview**：独立小节或已声明省略理由；启动 / 浏览 / 壳图或占位齐全（§3.5）  
- [ ] **README 本地预览壳**：`preview-readme.{html,css,js}` 已生成并绑定 `port-registry` 端口，或已声明省略（§3.5.1）  
- [ ] Showcase 路径或占位已写  
- [ ] **目录结构 / 仓库树 / Key docs 摘要直接呈现**（无 `<details>` 折叠）  
- [ ] 快速开始可执行；演示依赖写清  
- [ ] 未与 CONTEXT / LANGUAGES 抢事实源  

---

## 4. 体系化主 Prompt（复制给 Agent 用）

```text
你正在对仓库 {REPO_PATH} 执行 project-init。
严格按 project-init.md：Phase A → Phase B（README Polish）→ Gate。
每阶段结束先停，等我 Review。

## Phase A — 资产 · 融合 · 对齐
0. 同步 Cursor MDC Rules（§2.1）：从用户级复制 `windows-path-discipline.mdc` + `windows-shell-discipline.mdc` + `answer-format.mdc` + `AGENTS.mdc` + `commit-history.mdc` 到项目 `.cursor/rules/`。
1. 先与我确认：Issue tracker、triage、单/多 CONTEXT、外部资产清单、产品层根目录、项目预期、handoff 形式（覆盖式快照，见目标仓 `docs/agents/workflow.md` / `deliver.md`；**不要假设**存在 `docs/agents/handoff.md`）。
2. 运行 setup-matt-pocock-skills（一次只确认一项，确认后再写盘）。
3. 落盘根入口：AGENTS / CLAUDE / CONTEXT / LANGUAGES /（CONTEXT-MAP）/ README 初稿；
    在 AGENTS.md / CLAUDE.md 顶部引用 `humanizer-tta` skill（见 §2.9）；
    若 §2.2 B组#6 启用，另产出 `docs/agents/voice.md`（项目级输出语气与格式规范，覆盖全局 humanizer）。
4. docs 骨架：agents（仅 workflow/deliver/archive/domain/issue-tracker/triage-labels）、
   adr、knowledge、glossary、outputs/{report,prd,handoff,commit-history}。
   不要创建 docs/agents/language.md 或 docs/agents/context.md。
5. assets 骨架：backup · images/{readme,avatar,icon} · video · ppt · speeches · assets/README.md。
   禁止 docs/images/；旧图迁到 assets/images/readme。
6. 外来 zip/图/文按规范融合；迁移清单给我确认。
7. **Full 模式（老项目）**：启动 Agent 并行调研（§2.4.1），5 个维度分析项目，结果填充到 CONTEXT.md。
8. 本阶段不写业务功能代码。

## Phase B — README Polish
1. 加载 readme-polish skill。
2. 范文：xianghai-yuntu / ResumeWise / web3career-study-track / civil-service-exam-tracker；
   含金量标杆：agent-cfo。按本仓领域改写，禁止照抄。
3. 覆盖：结构 · 样式 · 配图 · Preview · Showcase（可占位）。
4. 若为资产库 / 多 demo：README 必须有 Preview 小节（启动 · URL · 浏览方式 · preview-shell 或占位）；
   与 Showcase 分开，不要混用文件名。
5. brief → docs/outputs/prd/readme-diagrams/；图 → assets/images/readme/。
6. 我负责出图；你负责 Prompt、落盘路径与 README 引用。
7. **硬样式**：目录结构 / 仓库树 / 结构摘要 / Key docs **禁止** `<details>` 折叠，必须直接呈现（见 readme-polish Step 4）。

## 门禁
- 每阶段停点汇报走 **Dual-Track**：先给结论（做了什么 / 卡在哪 / 下一步），再给证据表（改了哪些路径、怎么 Review）。
- 每轮末尾附 §0.4 两列表格（本轮做了什么 / 刚又完成）+ 一句感想小心思；全程融入 emoji+颜文字组合（代码块内不放）。
- 未经确认不要 git commit；不要跳过 Gate 直接写业务实现。
```

---

## 5. 日常业务流（init 完成之后）

```text
Issue(Epic) → docs/outputs/report/{theme}/   # 调研（可选）
  → docs/outputs/prd/{theme}/prd.md (draft)
  → 你 approved
  → docs/outputs/handoff/{theme}/YYYY-MM-DD-{branch}-{task}.md
  → 实施 → awaiting-review【停】
  → 你通过 → commit / docs/outputs/commit-history/{branch}/YYYY-MM-DD.md / archive
```

硬约束：PRD 未批准不写功能代码；handoff 覆盖式更新（旧文件直接删除）；Review 先于 commit。详见 `AGENTS.md` / `workflow.md`。

### 本仓 workbench 新建主题（可选附录 · 非通用）

> **仅当目标仓是 agentic-workbench（或明确声明有 `workbench/` + `port-registry`）时才执行。**  
> 对 Firefly / 普通个人站 / 无 workbench 的仓：**跳过整节**，勿创建 `docs/output/prd/port-registry.md` 或虚造 workbench 路径。

| 步骤 | 做法 |
|---|---|
| 1 | 在 `workbench/README.md` 看清 Kind（**资产** vs **模板**），复制**同类 peer** 骨架 |
| 2 | 对齐本文件的五件套与 `docs/` · `assets/` · 产品层；排除 `node_modules` 等 |
| 3 | 在 `docs/outputs/prd/port-registry.md`（或该仓既有 registry 路径）登记端口 |
| 4 | 更新 `workbench/README.md` 主题表 |

**不做**：恢复根级 `workbench/_template/` 生成器；模板主题勿把上游内部 AGENTS 提升进根治理。

---

## 5.0 Bug Issue 管理范式

> 发现的 Bug 统一走 Issue（GitHub 或本地 `.scratch/`），包含根因分析、复现步骤与修复 Agent 接手引导。与全局 skill `project-init` 执行面保持一致。

### 角色分工（诊断 → 修复 分离）

| 阶段 | 模型 | 产出 |
|------|------|------|
| 发现 | 用户 / 自查 | 问题描述 |
| 诊断 | OpenCode · DeepSeek（或等价） | 根因定位 + 复现脚本 + Issue 撰写 |
| 修复 | Claude Code · GLM（或等价） | 代码修复 + 复现验证 + commit |
| Review | 用户 | 验收关闭 |

### Issue 模板（8 段标准结构）

```markdown
## 问题描述
<!-- 用户视角，1-3 句 -->

## 根因
<!-- 技术视角：文件、行号、机制 -->

## 复现
### 自动化复现（如有脚本）
### 手动复现

## 关键代码位置
| 文件 | 行号 | 问题 |

## 修复方向（供修复 Agent 参考）

## 接手 Agent 引导
<!-- 1. 怎么复现  2. 怎么修  3. 怎么验证  4. 提交流程 -->
```

### 相关路径

- 复现脚本：`scripts/repro-*.mjs`（可反复运行验证）
- Issue 编号写入 commit body（`Closes #N`）
- 修复完成后 Issue 补充实际方案与验证结果

### 反模式

- ❌ Bug 修完不写 Issue（丢失根因与决策链）
- ❌ Issue 只有标题 + 一句话
- ❌ 同一模型既诊断又修复（缺乏交叉验证）

---

## 5.1 commit-history 维护规范

> `docs/outputs/commit-history/` 是 commit 攒批的**面向分支的可读摘要**，按分支组织，给"只看代码之外的人"快速了解每个分支干了什么。不是 git log 的复制，不逐条翻译 commit。

**何时写**
- 每个分支一轮 Review 通过、原子 commit 之后。
- 多个小 commit 可合并为一条摘要。

**目录结构**

```text
docs/outputs/commit-history/
├── main/
│   └── YYYY-MM-DD.md          ← 日期前缀，持续更新
├── feat-xxx/
│   └── YYYY-MM-DD.md
└── archive/                   ← 已合并到主分支的旧分支归档
    └── feat-old/
        └── YYYY-MM-DD.md
```

**文件命名**

```text
docs/outputs/commit-history/{branch}/YYYY-MM-DD.md
```

**表格格式（固定规范）**

| 日期 | 分支 | commit hash | 类型 | 主题 | 描述 |
|---|---|---|---|---|---|
| YYYY-MM-DD | main / feat-xxx | a2635a2 | feat/fix/docs/chore | 简明描述 | 详细说明 |

**字段模板**

```markdown
# {branch} · {date}

## Status
shipped | partial | reverted

## Commits

| 日期 | 分支 | commit hash | 类型 | 主题 | 描述 |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

## 做了什么
3–5 句主题摘要（不是逐 commit 翻译）。

## 关联
- PRD / handoff / Issue 路径
- 关键文件

## 回滚
- revert 哪几个 hash / 配置开关
```

**分支归档**
- 分支合并到主分支后，该分支文件夹移入 `archive/`。
- 主分支（main）永不归档。

**谁写**
- 执行 Agent 在 commit 后起草。
- 用户 Review 时校对，可要求 Agent 补全。

**反模式**
- ❌ 只贴 git log，无主题摘要。
- ❌ 记录无关 commit（纯格式化 / chore）。
- ❌ 长期不更新（本仓此前即处于此空壳状态）。
- ❌ 任务分支（task branch）写入 commit-history（只记主分支和特性分支）。

---

## 6. 一页 Checklist

### Phase A

- [ ] `.cursor/rules/` 五份 MDC 已落盘且 `alwaysApply: true`（含 `answer-format.mdc` + `AGENTS.mdc` + `commit-history.mdc`）
- [ ] 需求 / tracker / CONTEXT 形态 / 外部资产清单已与用户确认
- [ ] `setup-matt-pocock-skills` 完成并写盘
- [ ] 根：`AGENTS` / `CLAUDE` / `CONTEXT` / `LANGUAGES` /（`CONTEXT-MAP`）；AGENTS/CLAUDE 已引用 `humanizer-tta` skill + Windows Rules + Answer Format
- [ ] `docs/agents` 无 language.md、无 context.md
- [ ] `docs/outputs/prd` · `handoff` · `commit-history` · `report`
- [ ] `assets/` 就绪；外部资产已融合或迁移关闭
- [ ] 分端 CONTEXT（若需要）
- [ ] **Full 模式（老项目）**：Agent 并行调研完成，`CONTEXT.md` 已填充项目分析结果（§2.4.1）

### Phase B · README Polish

- [ ] `readme-polish` 已执行  
- [ ] 结构 · 样式达标；范文意图对齐  
- [ ] `assets/images/readme/` 契约图或占位说明  
- [ ] **Preview** 小节（或已声明本仓省略）· `preview-shell` / 启动命令  
- [ ] **README 本地预览壳** `preview-readme.{html,css,js}`（或已声明省略）· 端口对齐 `port-registry`  
- [ ] Showcase 路径 / 占位  
- [ ] 快速开始可跑  

### Gate

- [ ] 全程输出符合 §0.5 输出格式（轮末两列表格 / 双轨汇报 / 表情组合 / humanizer-tta 称呼）  
- [ ] 你已 Review init 产物  
- [ ] 允许开启第一个业务 theme  

---

## 7. 相关路径速查

| 资源 | 路径 |
|---|---|
| 本规范 | 根或 `docs/knowledge/project-init.md` |
| 共享词汇 | 根 `LANGUAGES.md` |
| 领域事实 | 根 `CONTEXT.md` |
| 界面术语库 | `docs/glossary/frontend-ui.md` |
| 任务流 | `docs/agents/workflow.md` |
| 调研报告 | `docs/outputs/report/{theme}/` |
| PRD | `docs/outputs/prd/{theme}/` |
| Handoff | `docs/outputs/handoff/{theme}/`（覆盖式更新，旧文件直接删除） |
| Commit 攒批 | `docs/outputs/commit-history/{branch}/`（按分支组织，表格格式） |
| Bug Issue 范式 | 本文档 §5.0；全局 skill `~/.claude/skills/project-init/SKILL.md` |
| 演示文稿 | `assets/ppt/` |
| 逐字稿 | `assets/speeches/` |
| 配图输出 | `assets/images/readme/`（含 `preview-shell.png` · `showcase-*.png`） |
| README 本地预览壳 | 主题/根 `preview-readme.{html,css,js}`（端口见 `port-registry`；规范见本文档 §3.5.1） |
| 上游备份 | `assets/backup/` |
| README Polish skill | `readme-polish` |
| 范文 | xianghai-yuntu · ResumeWise · web3career-study-track · civil-service-exam-tracker · **agent-cfo** |

---

## 8. 与上一版差异（迁移备忘）

| 旧约定 | 新约定 |
|---|---|
| Phase B + Phase C | 合并为 **Phase B · README Polish** |
| `docs/agents/language.md` · `context.md` | **删除**；只用根 `LANGUAGES.md` · `CONTEXT.md` |
| `docs/history/` | `docs/outputs/commit-history/` |
| `docs/output/reports/` | `docs/outputs/prd/` |
| `docs/images/readme/` | `assets/images/readme/` |
| `assets/theme/{ppt,script}/` | `assets/{ppt,speeches}/`（ADR 0018，冲突时以最新规范为准） |
| README 与 Showcase 分两阶段叙述 | 同属 README Polish |
| README 仅 Showcase 截图 | 增加 **Preview** 模块：本地预览站展示设计（与 Showcase 分工） |
| Bug 随手修、无 Issue | **§5.0 Bug Issue 范式**（诊断/修复分离 + 8 段模板） |
| 四份 MDC（Windows + answer-format + commit-history） | **五份 MDC**（+ `AGENTS.mdc`；`answer-format` 含白话 Mermaid，与用户级 `AGENTS.md` §16 对齐） |
| 无 Agent 并行调研 | **§2.4.1 Agent 并行调研**（Full 模式老项目专用，5 维度分析填充 CONTEXT.md） |
| README 目录树可用 `<details>` 折叠 | **禁止**：目录结构 / 仓库树 / 结构摘要 / Key docs **必须直接呈现**（与 `readme-polish` Step 4 一致） |
