# Product context

## 用户与问题

AgentCFO 服务 Web3 小团队和 DAO 的 Treasury 运营者。它解决贡献者结算依赖表格、审批链不透明、自动付款缺少安全边界的问题。

## 产品原则

- Agent 可以整理记录、生成计划和解释原因；
- Risk Engine 决定风险状态；
- Human Approval 决定是否进入执行；
- CAW 是真实资金执行边界；
- Audit Report 记录输入、决策、审批和执行证据；
- mock、simulation、testnet、real 必须明确标注。

## 当前 theme

`treasury-payout`

工作流：

```text
Issue
→ docs/outputs/report/treasury-payout/
→ docs/outputs/prd/treasury-payout/prd.md
→ 用户批准
→ docs/outputs/handoff/treasury-payout/
→ 实施
→ awaiting-review
```

## 事实来源

产品首页以 `README.md` 为入口。任务状态以 `docs/pm/` 为历史来源，新 theme 状态以 `docs/outputs/` 为准。契约以代码与测试为准（见根 `CONTEXT.md`）。
