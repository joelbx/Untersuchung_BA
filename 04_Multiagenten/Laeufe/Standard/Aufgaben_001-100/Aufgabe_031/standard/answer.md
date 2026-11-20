Fixed the default-config path. `config.Load("")` now applies `FLIPT_` environment overrides to defaults, and startup calls the loader even when no config file is found. File values still form the base when a path is provided.

Added regression tests for `FLIPT_LOG_LEVEL`, `FLIPT_SERVER_HTTP_PORT`, and file precedence. `go test ./internal/config ./cmd/flipt` passes.