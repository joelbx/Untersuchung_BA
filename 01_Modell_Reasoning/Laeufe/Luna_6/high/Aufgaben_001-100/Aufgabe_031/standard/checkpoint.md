# Checkpoint

Implemented `config.Load` handling for an empty path: it skips file reading, then populates defaults and unmarshals environment overrides. Config-file loading remains the base when a path is supplied, with env vars taking precedence.

Added regression coverage for default log level and HTTP port, `FLIPT_LOG_LEVEL` and `FLIPT_SERVER_HTTP_PORT` overrides (including integer parsing), and env precedence over file values.

Validation passed: `go test ./internal/config` and `git diff --check`.
