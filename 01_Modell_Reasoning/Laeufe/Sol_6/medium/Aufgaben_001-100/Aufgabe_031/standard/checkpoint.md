Task: Fix config.Load and CLI startup so FLIPT_ environment overrides apply with and without a config file.
Status: Implemented. Load skips file reading for an empty path while keeping defaults, environment binding, decoding, and validation. CLI always uses Load. Added tests for default values and env precedence, and switched existing env coverage to exercise Load("").
Verification: GOPROXY=off GOSUMDB=off go test ./internal/config ./cmd/flipt passed. git diff --check passed. Restored incidental go.work.sum changes.
