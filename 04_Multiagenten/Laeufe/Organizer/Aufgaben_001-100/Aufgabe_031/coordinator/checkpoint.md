# Checkpoint
Resolved: config.Load("") now uses Viper defaults and environment binding without reading a file.
CLI buildConfig now calls config.Load for file and no-file paths.
Added tests for defaults, environment overrides, and file-plus-environment precedence.
Verified: GOPROXY=off GOSUMDB=off go test ./internal/config ./cmd/flipt passed; git diff --check passed.
No delegation used.
