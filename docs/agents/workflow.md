# Agent workflow

> 对齐 Matt Pocock 系技能（`to-prd` · `to-issues` · `triage` · `handoff` · `grill-me`）与全局 `project-init` §5。  
> **不要假设**存在 `docs/agents/handoff.md`；任务 handoff 落在 `docs/outputs/handoff/`。

## 标准流程

```text
Issue（GitHub）
→ docs/outputs/report/{theme}/     # 调研可选
→ docs/outputs/prd/{theme}/prd.md  # draft
→ 用户 approved
→ docs/outputs/handoff/{theme}/YYYY-MM-DD-{branch}-{task}.md
→ 实施
→ 验证
→ awaiting-review
→ 用户通过
→ commit / docs/outputs/commit-history/{branch}/YYYY-MM-DD.md / archive
```

## 路径

| 产物 | 路径 |
| --- | --- |
| 调研 | `docs/outputs/report/<theme>/` |
| PRD | `docs/outputs/prd/<theme>/prd.md` |
| 任务交接 | `docs/outputs/handoff/<theme>/`（覆盖式：旧文件直接删除） |
| 决策 | `docs/adr/` |
| commit 攒批 | `docs/outputs/commit-history/<branch>/` |
| Bug Issue 范式 | `docs/knowledge/project-init.md` §5.0 |

旧写法 `docs/output/`（单数）与顶层 `docs/commit-history/` 已废弃；见各目录 stub。

## 当前配置

- Issue tracker：GitHub Issues（`docs/agents/issue-tracker.md`）
- Triage：Matt 五 canonical 状态（`docs/agents/triage-labels.md`）
- Context：多 Context（根 `CONTEXT-MAP.md`）
- Handoff：默认场景 A（业务任务实施前交接）；可用全局 `handoff` skill 压缩会话
- 首个 theme：`treasury-payout`

## Gate

- Project Init：Phase A → Phase B（README Polish）→ Gate；Gate 前不大规模业务编码
- 业务：PRD 未获用户批准时，不写该 theme 的功能代码；实施完成后停在 `awaiting-review`，用户 Review 先于 commit

## Matt 技能挂钩

| 意图 | Skill | 本仓消费文件 |
| --- | --- | --- |
| 拆垂直切片 Issue | `to-issues` | `issue-tracker.md` · `domain.md` · `triage-labels.md` |
| 从对话出 PRD | `to-prd` | 同上；产出进 tracker 或 `docs/outputs/prd/` |
| 分诊状态机 | `triage` | `triage-labels.md` |
| 锐化需求 | `grill-me` / `grilling` | 决策写入 `CONTEXT.md` / ADR |
| 会话交接 | `handoff` | 建议同步落盘 `docs/outputs/handoff/` |

## 现有流程兼容

`docs/pm/`、`docs/backend/`、`frontend/docs/` 继续作为历史与领域专项入口。新业务主题从 `docs/outputs/` 开始，不机械搬迁旧文件。
