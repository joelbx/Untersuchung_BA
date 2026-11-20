Fixed config loading so `config.Load("")` applies `FLIPT_` environment overrides to defaults, and the CLI uses that loader when no config file is found. File values still take precedence over defaults, while environment values take precedence over both. Added tests for `FLIPT_LOG_LEVEL` and `FLIPT_SERVER_HTTP_PORT`.

Verified with `go test ./internal/config ./cmd/flipt`.