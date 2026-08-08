# README images

根 `README.md` 的展示图片统一放在这里。范式对齐：

- [fork-Firefly `assets/images/readme/`](https://github.com/Aafff623/fork-Firefly/tree/main/assets/images/readme)
- 全局 / 仓内 [readme-polish](../../docs/knowledge/readme-polish/SKILL.md) 契约

## 命名契约

| 文件 / 模式 | 用途 | 制作 |
|---|---|---|
| `banner.png` | 页首横幅（团队黑客集体海报 · 3D 二次元定妆） | 设计图；旧黑金信息图见 git 历史 |
| `features.png` | 功能一览说明图 | 说明图（非 UI 冒充） |
| `workflow.png` | 业务主链路 | 说明图 · 决策点清晰 |
| `architecture.png` | 系统分层 / 拓扑 | 说明图 · 单一架构风格 |
| `tech-stack.png` | 技术栈 | 说明图 · 与 architecture 分工 |
| `landing-*.png` | Landing Showcase（本仓命名） | **真机截图** |
| `console-*.png` | Console Showcase（本仓命名） | **真机截图** |
| `showcase-*.png` | Firefly 风格通用名（可选迁移别名） | 真机截图 |
| `preview-shell.png` | Preview 产品壳 | 本仓**不需要**（无独立 Preview 站） |

## 当前资产

- ✅ `banner.png`（团队黑客集体海报）
- ✅ `landing-*.png` · `console-*.png`（Showcase）
- ⏳ `features.png` · `workflow.png` · `architecture.png` · `tech-stack.png`（见 `docs/outputs/prd/readme-diagrams/`）

团队头像在 [`../avatar/`](../avatar/)，不放本目录。

## 规则

- Showcase **必须**来自真实界面（Playwright / 实机）；禁止文生图冒充产品 UI
- 说明图遵守 4–6 色、统一描边、正交连线（readme-polish visual-standards）
- mock / testnet / real 在截图或说明中可辨
- 替换时保持稳定文件名，避免 README 断链
- 不提交 API key、私钥、未脱敏钱包或后台账户截图
- **禁止** `docs/images/`；终稿只在本目录
