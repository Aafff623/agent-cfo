# Delivery rules

## 交付状态

每个任务只使用以下状态：

```text
draft → approved → in-progress → awaiting-review → accepted → archived
```

`blocked` 可附加在任一未完成状态，并写清阻塞原因与解除条件。

## Handoff 最小字段

每份 `docs/outputs/handoff/<theme>/…md` 必须包含：

1. 目标和非目标；
2. 允许修改的路径；
3. 契约或安全不变量；
4. 实施步骤；
5. 验证命令；
6. 当前状态；
7. 用户 Review 条件。

命名建议：`YYYY-MM-DD-{branch}-{task}.md`。同一任务新快照**覆盖式**更新（删除旧 handoff 文件，避免双真相）。

不要假设存在 `docs/agents/handoff.md`。

## AgentCFO 验证

- 前端：`pnpm typecheck`，必要时 `pnpm build`
- 后端：`python -m pytest -q`（或仓库约定的等价命令）
- 文档：链接、路径、事实口径和 Markdown
- 资产：文件存在、命名、来源、许可；路径以 `assets/ASSET-MAP.md` 为准
- CAW：只在明确授权的 testnet 环境验证，不把 mock 当链上证据
- 契约分歧：以 `app/models.py` · `app/routers/payments.py` · `tests/test_mvp_flow.py` 为准

## 提交

只有用户明确要求时才 commit。一个 commit 只包含一个角色域和一个意图。提交前按 `.cursor/rules/commit-history.mdc` 维护 `docs/outputs/commit-history/{branch}/`；检查远端领先提交。
