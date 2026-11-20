Updated configuration loading so `Load("")` uses defaults and applies `FLIPT_` environment overrides. CLI startup now uses that path when no config file is found, and environment values still override file values.

Added regression coverage for `FLIPT_LOG_LEVEL`, `FLIPT_SERVER_HTTP_PORT`, defaults when those variables are absent, and precedence over file values.

Tests passed: `go test ./internal/config ./cmd/flipt`. `git diff --check` passed.

Changed [config.go](/app/internal/config/config.go:63), [main.go](/app/cmd/flipt/main.go:186), and [config_test.go](/app/internal/config/config_test.go:797).