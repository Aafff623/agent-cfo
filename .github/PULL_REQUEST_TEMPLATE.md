## Summary

<!-- 为什么改；一两句即可 -->

## Scope

- [ ] `frontend/` (Console / Landing — Landing 默认锁定)
- [ ] `app/` / `tests/` (API · Risk · CAW)
- [ ] `docs/` / `assets/` / repo meta

## Checklist

- [ ] 未发明后端契约外的 endpoint / field（真相：`app/models.py`）
- [ ] mock / real 行为说明清楚；默认仍是 mock-safe
- [ ] 未提交密钥、`.env`、私钥或未脱敏截图
- [ ] 本域验证跑过：前端 `pnpm typecheck`；后端 `pytest`（按改动勾选）
- [ ] Demo 数据一致（Bob = blocked）

## Test plan

<!-- 本地怎么验：例如 PORT=3100 pnpm dev + uvicorn :8000 -->
