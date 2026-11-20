Fixed default configuration loading. `config.Load("")` now applies `FLIPT_` environment overrides to defaults, and the command uses that loader when no config file is found. An absent Linux default config file also falls back to defaults.

Added regression cases for default and file based values with and without overrides. `go test ./internal/config ./cmd/flipt` passes.