Fixed the default config path. `config.Load("")` now applies environment overrides to defaults, and CLI startup uses the loader even when no config file is found. Added tests for `FLIPT_LOG_LEVEL` and `FLIPT_SERVER_HTTP_PORT` with both empty and file paths.

`go test ./internal/config ./cmd/flipt` passed.