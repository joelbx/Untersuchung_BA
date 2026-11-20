# Checkpoint

Issue: default config loading must apply `FLIPT_` environment overrides, with environment values taking precedence over defaults and file values.

Findings: `config.Load` unconditionally called `ReadInConfig`, and CLI startup bypassed `config.Load` when no config file was found. The existing Viper setup already binds nested config keys using the `FLIPT_` prefix and dot-to-underscore replacer.

Changes: `config.Load("")` skips the file read but still applies all defaults and bound environment overrides. CLI startup now calls `config.Load` for both file-backed and default configuration.

Verification: `go test ./internal/config ./cmd/flipt` passed. `cmd/flipt` has no test files; package compilation succeeded. `git diff --check` passed.
