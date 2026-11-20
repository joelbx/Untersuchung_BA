Fixed the default-config path. `config.Load("")` now loads defaults and applies `FLIPT_` environment overrides, and the CLI calls it when no config file is found. Environment values also take precedence over file values, including when a variable is explicitly set to an empty string.

The config and CLI regression tests pass: `GOPROXY=off GOSUMDB=off go test ./internal/config ./cmd/flipt`.

I delegated loader investigation and config test coverage, then integrated the changes and verified the final patch.