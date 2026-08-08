# Triage labels

> 对齐 Matt `triage` skill 与 project-init 默认五态。旧版 `triage:product/design/frontend/...` **已废弃**（易与状态机混淆）。

## Canonical 状态角色（每个 Issue 恰好一个）

| Label | 责任 |
| --- | --- |
| `needs-triage` | 维护者待评估 |
| `needs-info` | 等待报告者补充信息 |
| `ready-for-agent` | 规格完整，AFK agent 可接 |
| `ready-for-human` | 需人类实现 / 合并判断 |
| `wontfix` | 不处理（含已实现冗余） |

GitHub 上可直接使用上述字符串，或前缀 `triage:`（如 `triage:needs-triage`）；映射保持一对一，勿自造第三套状态名。

## Category 角色（每个 Issue 恰好一个）

| Label | 含义 |
| --- | --- |
| `bug` | 坏了 |
| `enhancement` | 新功能或改进 |

可用仓库既有 `type:bug` / `type:feature` 作等价映射，但 triage 读写时要落到上表 category。

## AgentCFO 辅助标签（可选，非状态）

- 优先级：`priority:p0` · `priority:p1` · `priority:p2`
- Theme：`theme:treasury-payout`
- 域提示（协作用，**不替代**五态）：`area:frontend` · `area:backend` · `area:platform` · `area:docs` · `area:assets`

## 规则

1. 每个 Issue：一个 category + 一个状态角色。
2. 状态冲突时先问维护者，再动。
3. `to-prd` / `to-issues` 产出默认打 `ready-for-agent`（除非用户另指定）。
4. triage 评论须带 Matt 要求的 AI 免责声明（见全局 `triage` skill）。
