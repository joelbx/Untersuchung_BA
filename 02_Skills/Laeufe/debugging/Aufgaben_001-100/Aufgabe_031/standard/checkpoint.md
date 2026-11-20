# Checkpoint

Task: Fix `config.Load` so environment variables override defaults and file values.

Status: Fixed and verified. `rg` is unavailable locally; used `find` and `grep` for repository inspection.

Evidence: `cmd/flipt/main.go` calls `config.Default()` and skips `config.Load` when no file exists. `config.Load` always calls `SetConfigFile(path)` and `ReadInConfig()`, including for an empty path. Existing config keys use `server.http_port`, which Viper maps to `FLIPT_SERVER_HTTP_PORT` through the dot-to-underscore replacer. Hypothesis: the startup bypass and unconditional file read cause the missing overrides and empty-path failure.

Reproduction: Added `TestLoadEnvironmentPrecedence`; before the fix, `GOPROXY=off GOSUMDB=off go test ./internal/config -run '^TestLoadEnvironmentPrecedence$' -count=1` failed with `loading configuration: Config File "config" Not Found in "[]"` for both empty-path cases. The file override case passed.

Patch: Skip file reading for an empty path in `config.Load`; make CLI startup call `config.Load` whether or not a file was discovered. Viper's existing prefix, key replacer, env binding, defaults and validation remain in one path.

Verification: Focused regression test passed; `GOPROXY=off GOSUMDB=off go test ./internal/config -count=1` passed. Initial `go test ./cmd/flipt` found `err redeclared` after the startup refactor; removed the redundant declaration and reran the exact command successfully (`[no test files]`). `git diff --check` passed. Go tooling modified `go.work.sum`; restored it to HEAD because it was unrelated.

Constraints: local evidence only; no downloads or history/index changes.
