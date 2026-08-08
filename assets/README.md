# AgentCFO 交付资产

竞赛路演与提交用的**可交付资产**统一放在本目录。技术文档见 [`../docs/`](../docs/)。  
路径规范与债务见 [`ASSET-MAP.md`](ASSET-MAP.md)。**冲突时以最新 project-init 为准。**

## 目录结构（如实）

```text
assets/
├── backup/                 # 上游二进制只读备份
├── video/                  # 答辩 / Demo 视频
├── images/
│   ├── readme/             # README 配图 + Showcase（banner / showcase-*）
│   ├── avatar/
│   ├── icon/
│   └── console/            # Console 模块图（本仓扩展）
├── theme/                  # ⚠ 物理债务区（竞赛期路径）
│   ├── ppt/                # 现存 PPT；canonical 目标 → assets/ppt/
│   └── script/             # 现存讲稿；canonical 目标 → assets/speeches/
├── ppt/README.md           # 跳转说明（勿假装二进制已迁移）
└── ASSET-MAP.md
```

按需创建：空的 `avatar/` / `icon/` / `video/` 槽位不要用 `.gitkeep` 凑齐。禁止 `docs/images/`。

## 当前状态

| 资产 | 现存路径 | 状态 |
| --- | --- | --- |
| 路演 PPT（ppt-master） | `theme/ppt/agentcfo-pitch.pptx` | ✅ |
| 路演 PPT（物料同学 PDF） | `theme/ppt/material/agentcfo-pitch-material-team-v1.pdf` | ✅ |
| PPT 源工程 | `theme/ppt/agentcfo-pitch/` | ✅ |
| 路演与 Demo 讲稿 | `theme/script/` | ✅ |
| 答辩视频 | `video/agentcfo-demo.mp4` | ✅ |
| README Banner / Showcase | `images/readme/` | ✅ |
| Console 模块吉祥物 / 参考 | `images/console/` | ✅ |
| 团队头像 | `images/avatar/` | ✅ |
| 项目 Logo | `images/icon/` | ☐ 待正式源文件 |

## 投递与归类

未归类文件先放 `inbox/`（见 `inbox/README.md`），整理后迁入上表路径并删除 `inbox/` 原文件。

## Preview / Showcase（媒体侧）

- **Showcase 图**：`images/readme/showcase-*.png` 或既有 `landing-*.png` / `console-*.png`
- **Preview 站**：本仓为单产品应用，一般不单独建资产 Gallery；见根 `LANGUAGES.md`
- **preview-readme**：在仓库根，不属于 `assets/`

## 重新导出 PPT

```bash
python .claude/skills/ppt-master/scripts/svg_to_pptx.py assets/theme/ppt/agentcfo-pitch
```

导出写入 `assets/theme/ppt/agentcfo-pitch/exports/`。确认后复制到 `assets/theme/ppt/agentcfo-pitch.pptx`。
