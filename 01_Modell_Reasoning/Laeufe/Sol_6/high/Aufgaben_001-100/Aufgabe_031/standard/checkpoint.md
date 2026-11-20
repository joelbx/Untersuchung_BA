Task: Fix default configuration so FLIPT_ environment overrides apply without a config file.
Status: Complete. config.Load("") skips file reading and applies existing defaults, environment binding, decoding, and validation. buildConfig always calls Load; determinePath treats an absent Linux default config file as no file.
Validation: GOPROXY=off GOSUMDB=off go test ./internal/config ./cmd/flipt (pass); git diff --check (pass). Added config regression cases for absent environment keys, default overrides, file values, and file overrides.
Files changed: internal/config/config.go, internal/config/config_test.go, cmd/flipt/main.go.
