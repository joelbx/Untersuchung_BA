# Checkpoint

Implemented `config.Load(path) (*Result, error)` with separate `Config` and `Warnings` outputs. Deprecation detection runs after reading the file but before defaults, and checks explicit config-file keys for cache memory settings, database migrations paths, and `ui.enabled`. Updated the CLI to log returned warnings independently and added loader test coverage, including explicit false values and environment-only settings.

Verification: `go test ./internal/config ./cmd/flipt` passed. `git diff --check` passed.
