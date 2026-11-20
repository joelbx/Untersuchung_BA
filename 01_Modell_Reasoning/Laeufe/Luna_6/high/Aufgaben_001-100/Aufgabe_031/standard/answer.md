Updated [config.go](/app/internal/config/config.go) so `Load("")` skips file reading, loads defaults, and applies env overrides. Config files still provide the base when a path is supplied, with env vars taking precedence.

Added regression tests for default values, `FLIPT_LOG_LEVEL`, integer parsing of `FLIPT_SERVER_HTTP_PORT`, and env precedence over file values.

Verified with `go test ./internal/config` and `git diff --check`.