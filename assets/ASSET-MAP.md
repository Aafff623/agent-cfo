# Asset directory map

> **冲突时以最新 project-init 为准**（全局 skill / `docs/knowledge/project-init.md`）。  
> 本表区分 **canonical（规范目标）** 与 **on-disk（现存物理路径）**，禁止把未搬迁的路径写成「已经在新位置」。

## Canonical vs 现存

| 类型 | project-init canonical | 现存物理路径（本仓） | 说明 |
| --- | --- | --- | --- |
| 上游只读备份 | `assets/backup/` | `assets/backup/` | 已对齐 |
| README / Showcase 图 | `assets/images/readme/` | `assets/images/readme/` | 已对齐；含 `preview-*` / `showcase-*` 命名契约 |
| 团队头像与吉祥物 | `assets/images/avatar/` | `assets/images/avatar/` | 旧跳转：`assets/images/readme/team/` |
| Logo / 品牌图标 | `assets/images/icon/` | `assets/images/icon/` | 旧：`assets/design/` 跳转 |
| 视频 | `assets/video/` | `assets/video/` | 已对齐 |
| PPT / PDF / 源工程 | `assets/ppt/` | **`assets/theme/ppt/`** | **物理债务**：文件仍在 `theme/ppt`；新投递优先写 canonical，或继续写入现存并更新本表 |
| 演讲稿 / 逐字稿 | `assets/speeches/` | **`assets/theme/script/`** | **物理债务**：旧名 `script`；规范名 `speeches` |
| Console 模块图 | （产品约定扩展） | `assets/images/console/` | project-init 未强制；本仓保留 |

兼容跳转 README（不放二进制副本）：

- `assets/ppt/README.md` → 指向现存 `assets/theme/ppt/`（待物理迁移后改写）
- `docs/speak/README.md` → 指向现存 `assets/theme/script/`

## 资产进入流程

```text
inbox
→ 核对来源、许可、隐私与用途
→ 规范命名
→ 移入 canonical（若目录尚未创建则创建；过渡期可写入现存物理路径并改本表）
→ 更新 assets/README.md 和相关交付清单
→ 验证引用
→ 删除 inbox 原文件
```

## 维护规则

- 文档不得声称文件在 `assets/ppt/` 若磁盘上仍只在 `assets/theme/ppt/`；
- 禁止新建 `docs/images/`；
- 运行时镜像放 `frontend/public/`，源资产仍以 `assets/` 为准；
- 不提交 API key、私钥、访问 token、未脱敏钱包后台截图；
- mock、testnet、real 证据必须分开命名和描述。
