# Issue tracker

## 选择

AgentCFO 使用 GitHub Issues：

`https://github.com/San-Y108/agent-cfo/issues`

本地 `.scratch/` 不作为正式任务来源（临时草稿可放，不替代 Issue）。

PRs as a request surface：**off**（外部 PR 默认不进 triage 队列）。

## Issue 最小结构

对齐 project-init §5.0（Bug）与 Matt `to-issues` 垂直切片模板：

```markdown
## 问题描述
## 根因或背景
## 复现 / 证据
## 关键代码位置
## 修复方向
## 接手 Agent 引导
## 验收条件
```

## Bug 流程

```text
发现
→ 独立诊断（诊断模型）
→ Issue（八段结构）
→ 修复（修复模型，与诊断分离）
→ 自动化或手动复现验证
→ 用户 Review
→ commit（Closes #N）
```

详见 `docs/knowledge/project-init.md` §5.0。

## Theme 关联

属于业务 theme 的 Issue 必须链接：

- `docs/outputs/prd/<theme>/prd.md`
- 对应 `docs/outputs/handoff/<theme>/…md`

首个 theme：`treasury-payout`。
