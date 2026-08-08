# Pitch deck assets（现存物理路径）

> **本目录不是 canonical。**  
> project-init / [`ASSET-MAP`](../../ASSET-MAP.md) 的规范目标是 **`assets/ppt/`**。  
> 本路径为竞赛期遗留的 **on-disk / 兼容路径**；物理迁移完成前，读写二进制请用本目录。  
> 冲突时以 `assets/ASSET-MAP.md` 为准。

兼容 stub（无二进制副本）：[`assets/ppt/README.md`](../../ppt/README.md)。

## 当前资产

| 资产 | 路径 |
| --- | --- |
| 主 PPT | `agentcfo-pitch.pptx` |
| 物料 PDF | `material/agentcfo-pitch-material-team-v1.pdf` |
| ppt-master 源工程 | `agentcfo-pitch/` |
| 逐页 SVG | `agentcfo-pitch/svg_final/` |
| 演讲备注 | `agentcfo-pitch/notes/` |

## 修改流程

1. 阅读 `.claude/skills/ppt-master/SKILL.md`；
2. 修改 `agentcfo-pitch/` 源工程；
3. 检查设计规范、14 页 SVG 和演讲备注；
4. 导出到本地 `exports/`；
5. 人工 Review；
6. 更新主 `agentcfo-pitch.pptx`。

`exports/`、时间戳 backup 和 `.live_preview.lock` 是可重建的本地产物，不纳入版本控制。

## 事实边界

CAW 证据使用当前可核验的 2 笔 Sepolia/SETH testnet 交易。线上 Console 默认 mock。P2 能力必须标为 preview 或 simulation。
