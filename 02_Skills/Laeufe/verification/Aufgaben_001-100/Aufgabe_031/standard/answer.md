When no config file is found, startup now calls `config.Load("")`, so defaults and `FLIPT_` environment overrides go through the same loading path as file configuration. I added tests for log level and HTTP port overrides, including precedence over file values.

Verification: `go test ./internal/config ./cmd/flipt -count=1` passed; `cmd/flipt` has no test files.