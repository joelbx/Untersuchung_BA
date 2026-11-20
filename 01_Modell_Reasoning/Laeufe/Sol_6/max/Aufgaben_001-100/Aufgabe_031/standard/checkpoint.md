# Checkpoint

Task: Fix environment overrides when Flipt starts without a config file.

Implemented: `config.Load("")` skips file reading and applies the existing Viper defaults and FLIPT_ environment bindings. `buildConfig` now calls `config.Load` for the no-file case. Added config tests for defaults, individual and combined environment overrides, and file values with environment precedence. Added a CLI regression test for debug logging and HTTP port overrides without a config file.

Verified: `go test ./internal/config -count=1` and `go test ./cmd/flipt -count=1` passed with module downloads disabled. `git diff --check` passed. Incidental `go.work.sum` changes were restored.
