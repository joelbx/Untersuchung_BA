# Checkpoint

Issue: default configuration loading ignored environment overrides when no config path was supplied.

Changes: `config.Load("")` now skips file reading and proceeds through Viper defaults, bound `FLIPT_` environment overrides, unmarshalling, and validation. CLI startup now calls this path when no config file is found. Regression coverage verifies unset defaults, `FLIPT_LOG_LEVEL`, `FLIPT_SERVER_HTTP_PORT`, and environment precedence over file values.

Verification: `go test ./internal/config ./cmd/flipt` passed. `git diff --check` passed. Reverted the unrelated `go.work.sum` change produced by Go workspace testing.
