# Checkpoint

Task: Add configurable `log.grpc_level` with `ERROR` default while preserving existing logging settings.

Changes: Added `LogConfig.GRPCLevel`, its `Default()` value, and optional `log.grpc_level` loading in `Load(path)`. Updated the sample config and advanced fixture; added a direct default assertion. Existing logging fields remain intact.

Checks:
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./config`: passed.
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./config ./cmd/flipt`: passed (`cmd/flipt` has no test files).
- `git diff --check`: passed.

Tooling: `rg` unavailable (`/bin/bash: line 1: rg: command not found`); used local `find` and `grep`.
