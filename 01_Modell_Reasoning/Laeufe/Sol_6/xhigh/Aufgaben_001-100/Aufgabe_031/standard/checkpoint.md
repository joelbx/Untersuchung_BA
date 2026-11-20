# Checkpoint

Task: make environment variables override defaults when no config file is supplied, while preserving file-based overrides and the FLIPT_ uppercase underscore mapping.

Findings: `config.Load` required a config path and startup bypassed it entirely when no file was found. The existing Viper setup already binds configuration fields to `FLIPT_` environment variables.

Changes: `Load("")` now skips file reading and runs the same default, environment binding, decoding, and validation path. `buildConfig` always calls `Load`. Added focused coverage for defaults, individual and combined environment overrides, and file values with overrides.

Verification: `GOPROXY=off go test ./internal/config -run '^TestLoadEnvironmentOverrides$' -count=1` passed; `GOPROXY=off go test -mod=readonly ./internal/config ./cmd/flipt` passed. The incidental `go.work.sum` update from Go was restored.
