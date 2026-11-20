# Checkpoint

Resolved: `config.Load("")` now uses the normal Viper defaults, environment binding, unmarshalling, and validation flow without attempting to read a file. Startup calls `config.Load(path)` even when no file is found, so default startup respects `FLIPT_` overrides. Existing environment mapping remains `FLIPT_` plus uppercase keys with dots replaced by underscores.

Regression coverage: `TestLoadDefaultsAndEnvironmentOverrides` checks full defaults with an empty path, file base values, and overrides for `FLIPT_LOG_LEVEL` and `FLIPT_SERVER_HTTP_PORT` in both cases.

Checks passed: `go test ./internal/config ./cmd/flipt`; `git diff --check`.
