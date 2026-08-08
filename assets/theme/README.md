# Theme assets（现存物理 / 兼容树）

> **本树不是 canonical 落点。**  
> 映射与债务说明见 [`../ASSET-MAP.md`](../ASSET-MAP.md)。冲突时以 ASSET-MAP / 最新 project-init 为准。

```text
assets/theme/
├── ppt/      # 现存：路演 PPT / PDF / SVG / 源工程 → canonical 目标 assets/ppt/
└── script/   # 现存：路演稿 / Demo 逐字稿 → canonical 目标 assets/speeches/
```

物理迁移完成前，读写继续用上述现存路径。兼容 stub（无二进制副本）：[`assets/ppt/README.md`](../ppt/README.md)。

二进制成片继续放在 `assets/video/`。README 展示图继续放在 `assets/images/readme/`。
