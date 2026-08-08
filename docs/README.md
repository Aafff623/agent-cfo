# AgentCFO 文档索引

项目根目录 `docs/` 存放**文字类文档**（项目管理、技术边界、阶段报告）。竞赛交付用的 PPT、视频、海报等二进制资产放在 [`../assets/`](../assets/)。队友投递的未归类文件先放 [`../inbox/`](../inbox/)，整理后迁入 `assets/` 或 `docs/`。

## 目录

| 目录 | 用途 |
| --- | --- |
| [`backup/`](backup/) | README 等文档的**只读备份**（合并前快照） |
| [`backend/`](backend/) | 后端技术深文档（CAW、部署、P2；合并时从 README 拆出） |
| [`plans/`](plans/) | 规划文档（含 [README 合并规划](plans/README-merge-plan.md)） |
| [`pm/`](pm/) | 任务看板、站会、风险、提交清单、彩排、交付报告 |
| [`p2/`](p2/) | P2 扩展能力边界与设计说明 |
| [`reports/`](reports/) | 阶段性状态 / handoff 报告 |
| [`agents/`](agents/) | Agent workflow、交付、归档、领域、Issue、Triage、语气 |
| [`contexts/`](contexts/) | 多 Context 领域说明 |
| [`adr/`](adr/) | Architecture Decision Records |
| [`knowledge/`](knowledge/) | 可跨 theme 复用的知识 |
| [`glossary/`](glossary/) | 领域术语 |
| [`outputs/`](outputs/) | 新业务 theme 的 report、PRD、handoff、commit-history（**复数**；规范路径） |
| [`output/`](output/) · [`commit-history/`](commit-history/) | **已废弃 stub**，重定向到 `outputs/` |

路演、Demo 陈述稿和成员口述现存于 [`../assets/theme/script/`](../assets/theme/script/)（canonical 目标 `assets/speeches/`，见 [`../assets/ASSET-MAP.md`](../assets/ASSET-MAP.md)）。`docs/speak/` 仅保留兼容入口。

## 常用入口

- [README 合并规划](plans/README-merge-plan.md)
- [提交材料清单](pm/SUBMISSION_CHECKLIST.md)
- [Demo 彩排检查清单](pm/DEMO_REHEARSAL_CHECKLIST.md)
- [任务看板](pm/TASK_BOARD.md)
- [交付总控报告](pm/DELIVERY_MASTER_REPORT_2026-06-08.md)
- [P2 Demo Handoff](pm/P2_DEMO_HANDOFF.md)
- [路演陈述稿索引](../assets/theme/script/README.md)
- [Demo 视频录制指南](../assets/theme/script/demo-video-guide.md)
- [Demo 视频 Landing 接入规划](plans/demo-video-landing-integration-plan.md)
- [Agent workflow](agents/workflow.md)
- [Theme outputs](outputs/README.md)
- [多 Context 入口](../CONTEXT-MAP.md)

## 前端专项文档

前端开发过程中的 plans / handoff / UI 研究文档仍在 [`../frontend/docs/`](../frontend/docs/)，不与本目录的竞赛交付文档混放。
