# Checkpoint

Resolved the default-config environment override issue.

Changes:
- `internal/config/config.go`: `Load("")` skips file reading and continues through environment binding, defaults, unmarshalling, and validation.
- `cmd/flipt/main.go`: startup calls `config.Load(path)` even when no configuration file is found.
- `internal/config/config_test.go`: tests default values and FLIPT_LOG_LEVEL / FLIPT_SERVER_HTTP_PORT overrides for empty path and file path.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off GOFLAGS=-mod=readonly go test ./internal/config ./cmd/flipt -count=1` exited 0: internal/config passed; cmd/flipt has no test files and compiled.
- `git diff --check` exited 0.

Tooling note: `rg` unavailable (`/bin/bash: rg: command not found`); used local grep/find fallback. Go tooling initially added unrelated go.work.sum entries; restored its original working-tree contents. No downloads requested.
