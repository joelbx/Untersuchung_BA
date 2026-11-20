# Checkpoint

Implemented release.Is and release.Check in internal/release; startup consumes release.Info for update reporting and build metadata, and disables telemetry for CI and non-release builds. Added release classification and update comparison tests. Verified with `GOPROXY=off go test ./internal/release ./cmd/flipt ./internal/info` and `git diff --check`.
