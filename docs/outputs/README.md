# Theme outputs

新业务工作统一进入：

```text
docs/outputs/
├── report/<theme>/
├── prd/<theme>/
├── handoff/<theme>/
└── commit-history/<branch>/
```

有产物再建子目录；不要为空类预铺 `.gitkeep`。

## 状态流

```text
report（可选）
→ PRD draft
→ 用户 approved
→ handoff（覆盖式）
→ 实施
→ awaiting-review
→ accepted
→ commit-history
```

现有 `docs/pm/`、`docs/backend/`、`docs/reports/` 与 `frontend/docs/` 保持原位（历史/专项）。首个 theme：`treasury-payout`。

对齐：`docs/agents/workflow.md` · `docs/knowledge/project-init.md` §5。
