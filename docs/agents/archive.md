# Archive rules

## 归档原则

- 归档是保留事实，不是隐藏未完成项；
- 文件一旦成为外部链接目标，优先保留路径并增加索引；
- 旧文档不机械改写为当前状态；
- 需要替代时，在旧文件顶部指向新的事实来源。

## 归档位置

| 类型 | 路径 |
| --- | --- |
| README 历史快照 | `docs/backup/` |
| 上游二进制资产备份 | `assets/backup/` |
| 已完成 theme 的报告、PRD、handoff | 保留在 `docs/outputs/<type>/<theme>/` |
| commit 批次说明 | `docs/outputs/commit-history/{branch}/`；合并后分支移入 `…/archive/` |
| 前端 phase 历史 | `frontend/docs/handoff/`（Console 专项，非 project-init theme handoff） |

旧路径 `docs/output/`、顶层 `docs/commit-history/` 仅留重定向 stub。

## 完成条件

Theme 归档前必须：

1. 用户已 Review；
2. handoff 状态为 `accepted`；
3. 验证结果有证据；
4. 未完成项已转移到 Issue；
5. 入口索引已更新；
6. 未把密钥、私钥或内部凭证写入文档。
