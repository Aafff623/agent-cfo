# AgentCFO · 像素黑客风 Prompt 包（GPT 网页端）

> 用法：打开 GPT 图像能力 → **上传参考图**（路径见下）→ 粘贴对应 Prompt。  
> 标杆气质：`blog/Firefly` 的 `banner-pixel-garden.png`（高细节像素 + 人物右置 + 左场景叙事），题材换成 **DAO AI CFO / 黑客风金库**。  
> Showcase（`landing-*` / `console-*`）仍用真机截图，**不要**用本文重画 UI。

## 0. 参考图路径（本机绝对路径）

### 风格锚（先看一眼）

| 用途 | 路径 |
|---|---|
| Firefly 像素横幅标杆 | `D:\OneDrive\Desktop\blog\Firefly\assets\images\readme\banner-pixel-garden.png` |
| 现行 README banner（团队黑客集体海报 · 已采用） | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\readme\banner.png` |
| 替换前旧 banner | git 历史中上一版 `assets/images/readme/banner.png`（黑金信息图） |

### 产品主角色（优先上传）

| 角色 | 路径 |
|---|---|
| Agent CFO 主场景（紫发女孩 + 白银小球机器人） | `D:\OneDrive\Desktop\project\agent-cfo\frontend\public\console\mascots\agent-cfo-mascot.png` |
| Agent 模块 | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\console\module-mascots\agent-module-mascot.png` |
| Treasury 模块 | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\console\module-mascots\treasury-module-mascot.png` |
| Wallets 模块 | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\console\module-mascots\wallets-module-mascot.png` |
| Analytics 模块 | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\console\module-mascots\analytics-module-mascot.png` |
| Policy 模块 | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\console\module-mascots\policy-module-mascot.png` |
| 运行时镜像（同造型） | `D:\OneDrive\Desktop\project\agent-cfo\frontend\public\console\mascots\modules\*-module.png` |

### 团队 3D 吉祥物（像素化角色参考）

| 成员 | 路径 |
|---|---|
| threetwoa（金发黑技战术服 · 全息面板） | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\avatar\threetwoa-mascot.png` |
| ZanyK（探险马甲 · 罗盘地图 → 可改成指挥 HUD） | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\avatar\zanyk-mascot.png` |
| 欢（白科技紧身衣 · 全息图 + 手机清单） | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\avatar\huan-mascot.png` |
| 呱呱（奶油毛衣 · 发光笔 + 草图本 → 可改成设计终端） | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\avatar\guagua-mascot.png` |
| 九九八乂（蓝灰海豹 · 耳机 + 服务器背包 + 绿码平板） | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\avatar\jiujiu-mascot.png` |
| purple sun（白熊 · 紫链 + 紫色数据方块） | `D:\OneDrive\Desktop\project\agent-cfo\assets\images\avatar\purple-sun-mascot.png` |

角色头像（可选脸型辅助）：同目录 `*-role.jpg`。

### 落盘建议

| 产出 | 建议文件名 |
|---|---|
| README 页首 | `assets/images/readme/banner-pixel-treasury.png` |
| 团队像素立绘（可选） | `assets/images/readme/team/pixel-{slug}.png` |

---

## 1. 全局 Style Lock（每次先贴）

```text
STYLE LOCK — keep for the whole image:
- High-detail modern pixel art (indie-game cinematic pixel), NOT chunky 8-bit, NOT photoreal, NOT smooth 3D CGI
- Visible pixels but fine enough for facial expression, hair strands as pixel clusters, soft dithered shading
- Dark hacker / cyber-ops atmosphere: deep slate #0B1220 / near-black, neon accents
- AgentCFO palette accents ONLY: lime #B5FF4D, cyan #5EEAD4 / #22d3ee, soft violet #C084FC, coral warn #FB7185, amber #F59E0B
- Hacker props allowed: translucent HUD panels, terminal green scanlines, cable trails, server rack silhouettes, shield/gate icons, wallet glyphs, approval stamps, risk diamonds — keep them scenic, not an infographic collage
- NO fake realistic tx hashes as readable microtext, NO coin rain, NO dollar-bill confetti, NO glassmorphism stock crypto poster, NO watermark, NO logos of real brands
- Preserve uploaded character identity (silhouette, hair, outfit colors, signature props) while converting medium from 3D toy/CGI to pixel art
```

---

## 2. README 主 Banner（最重要 · 先生成这个）

**上传顺序建议（最多 4 张）：**

1. `banner-pixel-garden.png`（只要构图/像素工艺，不要抄中世纪城堡）
2. `agent-cfo-mascot.png`（主角色身份）
3. `treasury-module-mascot.png`（Treasury / Audit 气质）
4. 可选一张团队图：`threetwoa-mascot.png` 或 `jiujiu-mascot.png`（点缀角色）

**Aspect：21:9 或 3:1 · 横幅**

```text
Create a premium GitHub README hero banner for AgentCFO — a DAO AI CFO with a controlled wallet.

FORMAT
- Exact wide banner 21:9 (or 3:1), edge-to-edge scene, suitable as README header
- High-detail modern pixel art, indie cinematic pixel look
- Dark hacker treasury command-room at night

COMPOSITION (mirror Firefly banner structure, change subject)
- RIGHT third: main heroine — purple high ponytail anime girl in black techwear hoodie, fingerless gloves, over-ear headphones with neon accents; confident, calm operator pose looking left into the room
- Beside her (slightly lower): small chibi white-silver orb robot companion with glowing purple oval eyes and tiny antenna ears
- LEFT two-thirds: deep cyber treasury chamber — server racks as silhouette, floating translucent HUD frames connected by thin neon node lines (workflow nodes: Plan → Risk → Approval → Wallet → Audit), a glowing lime “approval gate”, a cyan shield, a coral “blocked” diamond off to a side branch
- Floor: reflective dark tiles with faint lime/cyan scanlines; sparse floating firefly-like data sparks (tiny pixels), not coin rain
- Optional tiny cameo (far left midground, small): pale blue seal with headset + server backpack (backend vibe) OR blonde agent in black suit with cyan HUD — keep secondary, do not crowd the heroine

PALETTE
- Base: #0B1220 / black
- Accents: lime #B5FF4D, cyan #5EEAD4, violet #C084FC, coral #FB7185
- Warm gold only as tiny terminal cursor / coin-medallion glow (one focal, not everywhere)

MOOD
- Hacker-ops elegance: controlled power, auditability, human-in-the-loop — not chaotic cybercrime, not meme crypto
- Feels like “pixel anime operator in a secure treasury NOC”

HARD NEGATIVES
- No photoreal hands, no 3D plastic toy shading, no corporate black-gold infographic cards around a dollar logo
- No dense readable paragraphs, no fake dashboards filling half the banner with English walls of text
- No medieval castle/moon garden (that was only a composition reference)
- No watermarks, no real brand logos, no QR codes
```

**中文补钉（可贴在英文后）：**

```text
高细节像素风横幅，紫发黑客少女与白色小球机器人在右侧；左侧是深色金库指挥室与半透明 HUD 节点连线；主色 lime/cyan/violet；禁止金币雨与假交易哈希墙。
```

---

## 3. 团队像素立绘（单角色 · 透明/纯黑底）

每次只上传 **1 张对应 mascot** + 可选 Firefly banner（只要像素工艺）。Aspect：**1:1**。

### 3A · threetwoa

参考：`assets/images/avatar/threetwoa-mascot.png`

```text
Convert the uploaded 3D chibi character into high-detail pixel art, full body, plain near-black background.

KEEP IDENTITY
- Short blonde side-swept hair, cyan glowing eyes, black tactical suit with cyan collar/chest neon, half-cape coat tails, palms up with cyan grid on hands
- One floating cyan holographic UI panel with a small warning triangle (abstract icons only)

HACKER UPGRADE
- Add subtle scanline on the HUD, tiny cable from belt pack, lime status LED on collar
- Serious operator expression

STYLE: modern cinematic pixel art, clean silhouette, no text paragraphs, no watermark
```

### 3B · ZanyK（指挥总控 · 把探险道具改黑客指挥）

参考：`assets/images/avatar/zanyk-mascot.png`

```text
Convert the uploaded blonde chibi explorer into high-detail pixel art hacker-commander, plain near-black background.

KEEP: big head chibi proportions, blonde swept hair, friendly determined face, olive tactical vest silhouette
REPLACE PROPS: compass → glowing cyan tactical rangefinder/HUD disc; map → translucent lime workflow slate showing node path Plan-Risk-Approve
ADD: earpiece mic, small amber “lead” badge LED on vest
Palette accents: lime + cyan on dark olive/khaki
Modern cinematic pixel art, no readable microtext walls, no watermark
```

### 3C · 欢（PM）

参考：`assets/images/avatar/huan-mascot.png`

```text
Convert the uploaded dark-haired chibi in white tech suit into high-detail pixel art, near-black background.

KEEP: messy dark brown hair, focused eyes, white/silver tech suit, chest blue LED
PROPS: translucent cyan holographic roadmap tablet + black phone checklist UI (abstract ticks only)
HACKER ADD: soft violet underline on hologram title bar, tiny coral “blocked” chip icon on checklist
Modern cinematic pixel art, no watermark
```

### 3D · 呱呱（物料 / 设计）

参考：`assets/images/avatar/guagua-mascot.png`

```text
Convert the uploaded smiling girl with long wavy brown hair and cream sweater into high-detail pixel art, near-black background.

KEEP: cozy sweater silhouette, bright smile, big eyes
HACKER-CREATIVE UPGRADE: glowing stylus becomes neon-lime design probe; notebook becomes translucent violet UI moodboard panel with abstract wireframe boxes
Optional tiny pixel stickers floating (palette, pen, shield) — sparse
Modern cinematic pixel art, cute but not childish sticker sheet, no watermark
```

### 3E · 九九八乂（后端 / Agent）

参考：`assets/images/avatar/jiujiu-mascot.png`

```text
Convert the uploaded pale blue baby seal mascot into high-detail pixel art, near-black background.

KEEP: round seal body, rosy cheeks, silver-black headset with cyan rings, server-rack backpack, green code tablet
HACKER AMP: stronger terminal-green glow on tablet, thin data-stream particles (cyan/lime), vent LEDs on backpack
Expression earnest/cute; modern cinematic pixel art; abstract code blocks only (no readable secrets); no watermark
```

### 3F · purple sun（合约 / CAW）

参考：`assets/images/avatar/purple-sun-mascot.png`

```text
Convert the uploaded white polar-bear chibi into high-detail pixel art, near-black background.

KEEP: meditative sit pose, closed eyes, purple blush, black collar with glowing purple hex pendant, floating purple translucent data cube, purple chain accent
HACKER/CHAIN ADD: cube shows abstract block/node facets (blockchain vibe), faint cyan approval ring under the cube
Calm cyber-zen mood; modern cinematic pixel art; no watermark
```

---

## 4. 产品双人组（女孩 + 机器人 · 模块色变体）

上传：`agent-cfo-mascot.png` + 对应 `*-module-mascot.png`。Aspect：**1:1** 或 **4:3**。

```text
Create a high-detail pixel art duo portrait of AgentCFO characters on near-black background.

CHARACTERS (match uploads)
- Purple-ponytail anime girl in black techwear + headphones + fingerless gloves
- Small white-silver floating robot with purple oval eyes

SCENE PROP (one module only)
- Agent: cyan chat-bubble hologram
- Treasury: lime/cyan audit scroll hologram with shield + verified tick (abstract)
- Wallets: blue wallet glyph hologram + chain-link motif
- Analytics: violet chart hologram (simple bars/line)
- Policy: coral shield / guardrail gate hologram

Accent the module color strongly but keep lime as success tick.
Modern cinematic pixel art; no dense English UI text; no watermark.
```

---

## 5. GPT 网页端操作清单

1. 新建对话，先贴 **§1 Style Lock**
2. 上传参考图（Banner 用 §2 的 3–4 张；单角色用对应 1 张）
3. 粘贴目标章节 Prompt
4. 若不像像素：追加一句 `Increase visible pixel grid and dithering; reduce smooth 3D shading.`
5. 若太 8-bit：追加 `Finer pixels, more detail in hair and eyes, keep cinematic lighting.`
6. 导出 PNG → 落到 `assets/images/readme/banner-pixel-treasury.png`（或 team 子目录）
7. README 挂载改路径后，本地 `preview-readme.html` 复核

---

## 6. 验收

| 项 | 标准 |
|---|---|
| 一眼像素 | 有点阵与抖动，不是磨皮 3D |
| 黑客感 | HUD / 终端光 / 服务器剪影至少两类 |
| 角色可认 | 对照上传 mascot 发型/配色/标志道具仍在 |
| README 可用 | 横幅远处缩略仍能读出「人 + 金库场景」 |
| 合规 | 无假大额余额墙、无真实私钥/地址正文 |
