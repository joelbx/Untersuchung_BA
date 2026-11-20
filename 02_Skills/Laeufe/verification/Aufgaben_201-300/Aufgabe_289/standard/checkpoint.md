# Checkpoint

Task: Export canonical default configuration and decode hooks; keep loading behavior aligned; verify configuration and CUE schema.

Changes:
- Added `DefaultConfig() *Config` in `internal/config/config.go` using the defaults previously held in the config test helper.
- Exported `DecodeHooks` and used it in `Load` with the storage experiment skip hook.
- Added the `version` mapstructure tag.
- Changed storage `Local` and `Git` to pointers with nil-safe validation, and updated test expectations.
- Corrected `boolean` to CUE's `bool` in `config/flipt.schema.cue`.
- Added tests for exported hooks, duration decoding, and CUE schema compilation.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config -count=1`: passed (`ok go.flipt.io/flipt/internal/config 0.117s`).
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/cmd -run '^$'`: passed (`ok go.flipt.io/flipt/internal/cmd 0.010s [no tests to run]`).
- `rg` unavailable (`/bin/bash: line 1: rg: command not found`); used `find` and `grep`.

Limit: The local regression checks CUE schema compilation and decode hooks separately. The repository does not contain `internal/config/schema_test.go`, so its exact validation path has not been executed.
