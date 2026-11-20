Fixed the default configuration path. `config.Load("")` now applies `FLIPT_` environment overrides to defaults, and startup calls it when no config file is found. File-based configuration still uses environment values where they are set.

Added tests for default and file-based values, including `FLIPT_LOG_LEVEL` and `FLIPT_SERVER_HTTP_PORT`. `go test ./internal/config ./cmd/flipt` passed.