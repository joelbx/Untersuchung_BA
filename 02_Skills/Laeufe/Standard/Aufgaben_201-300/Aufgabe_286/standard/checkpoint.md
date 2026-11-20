# Checkpoint

Implemented release classification and update comparison in `internal/release/check.go`. Startup now uses `release.Is` and `release.Check`, reports current/latest version and update URL according to log encoding, and disables telemetry for non-release builds and CI. Added local tests for prerelease versions, update comparisons, and latest URL behavior.

Verification passed:
- `GOPROXY=off GOSUMDB=off go test ./internal/release`
- `GOPROXY=off GOSUMDB=off go test ./internal/release ./cmd/flipt ./internal/info`
- `GOPROXY=off GOSUMDB=off go test ./internal/telemetry ./internal/config`
- `git diff --check`
