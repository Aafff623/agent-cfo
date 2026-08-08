# Assets and delivery context

## 路径

- 待归类：`inbox/`
- 已归类资产：`assets/`（映射见 [`../../assets/ASSET-MAP.md`](../../assets/ASSET-MAP.md)）
- README / Showcase 图片：`assets/images/readme/`
- 前端运行时静态资源：`frontend/public/`
- 流程文档产物：`docs/outputs/`（非媒体）

## Canonical vs 现存（摘要）

| 规范目标（project-init） | 本仓现存 |
| --- | --- |
| `assets/ppt/` | `assets/theme/ppt/` |
| `assets/speeches/` | `assets/theme/script/` |

冲突时以最新 project-init 为准；文档不得假装文件已在 canonical 路径。

兼容跳转：`docs/speak/` → `assets/theme/script/`；`assets/ppt/README.md` → `assets/theme/ppt/`。

## 归档流程

```text
inbox
→ 核对来源、许可、用途
→ 重命名
→ 归档至 assets 或 docs/outputs（文档类）
→ 更新入口索引
→ 删除 inbox 原文件
```

不得把密钥、钱包私钥、API token 或未脱敏的账户截图放入资产目录。禁止 `docs/images/`。
