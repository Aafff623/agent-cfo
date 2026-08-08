# Inbox

`inbox/` 是临时投递区，不是长期资产目录。

## 使用规则

1. 新外部文件先放进 inbox；
2. 文件名必须能说明来源和用途，不使用 hash 文件名；
3. 核对许可、隐私、密钥和事实边界；
4. 按下表迁入目标路径（见 `assets/ASSET-MAP.md`）；
5. 更新资产索引和引用；
6. 验证后删除 inbox 原文件。

## 归类目标

| 类型 | 优先写入（现存可写） | project-init canonical |
| --- | --- | --- |
| README / Showcase 图 | `assets/images/readme/` | 同左 |
| 团队头像与吉祥物 | `assets/images/avatar/` | 同左 |
| Console 参考图 | `assets/images/console/` | 本仓扩展 |
| Logo 与品牌设计 | `assets/images/icon/` | 同左 |
| PPT、PDF 与源工程 | `assets/theme/ppt/`（现存） | `assets/ppt/` |
| 路演稿、Demo 文案 | `assets/theme/script/`（现存） | `assets/speeches/` |
| 视频 | `assets/video/` | 同左 |
| 不可重建的上游原件 | `assets/backup/` | 同左 |
| 产品与技术文档 | `docs/`（流程产物进 `docs/outputs/`） | — |
| 前端运行时镜像 | `frontend/public/` | — |

禁止新建 `docs/images/`。

## 当前状态

2026-06-13 已处理的历史原图已归档到：

`assets/backup/inbox-sources-20260613/`

当前 Git 跟踪的 inbox 只保留本说明文件。新投递应在一次任务内完成分类，不长期堆积。

## 禁止

- API key、私钥、访问 token；
- 未脱敏的钱包后台或账户截图；
- 未确认来源和许可的第三方素材；
- 与 canonical 资产重复的副本；
- 构建缓存和临时导出目录。
