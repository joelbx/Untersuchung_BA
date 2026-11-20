Fixed the default-config path: `config.Load("")` now applies `FLIPT_` environment overrides to defaults, and the CLI uses that loader when no config file is found. File-backed configuration still gives environment variables precedence. Added regression coverage for both paths.

`go test ./internal/config ./cmd/flipt` passed.