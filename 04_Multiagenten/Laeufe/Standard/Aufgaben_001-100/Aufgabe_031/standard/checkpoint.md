Task: Fix config.Load and startup so environment overrides apply when no config file is supplied.
Status: Complete.
Changes: config.Load skips file reading for an empty path while still applying defaults and bound FLIPT_ environment variables. Startup always calls config.Load. Added regression coverage for defaults, empty-path overrides, file overrides, and preserved file values.
Verification: go test ./internal/config ./cmd/flipt passed; git diff --check passed.
