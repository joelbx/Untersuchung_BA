# Checkpoint

Task: add `log.grpc_level` to runtime configuration with default `ERROR`, preserving existing log settings.

Implemented:
- `LogConfig.GRPCLevel` with JSON key `grpc_level`.
- `Default()` sets `GRPCLevel` to `ERROR`.
- `Load(path)` reads `log.grpc_level` when set.
- Documented the default and added coverage for default and explicit values.

Verification:
- Red phase: `GOPROXY=off go test ./config -run 'Test(DefaultGRPCLogLevel|Load)$' -count=1` failed to compile because `GRPCLevel` did not yet exist.
- Green phase: `GOPROXY=off go test ./config -count=1` passed (`ok go.flipt.io/flipt/config 0.004s`).
- `git diff --check` passed.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); local `find` and `grep` were used.
