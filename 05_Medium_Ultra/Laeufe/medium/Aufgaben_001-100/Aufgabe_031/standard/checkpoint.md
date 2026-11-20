Task complete: Default configuration now goes through config.Load, so FLIPT_ environment overrides apply with no config file. Explicit file loads keep file values as the base and environment values as overrides.
Changes: internal/config/config.go, cmd/flipt/main.go, internal/config/config_test.go.
Verification: go test ./internal/config ./cmd/flipt passed; git diff --check passed.
