# Checkpoint

Implemented the release separation and startup wiring:
- Added `internal/release` with release-candidate classification and the release check result (`current`, `latest`, update flag, and URL).
- Startup uses `release.Is` and `release.Check`; check failures warn and startup continues.
- Startup status uses colored console output for console encoding and structured logger output otherwise.
- `info.Flipt` retains current build metadata for all versions and now includes the latest release URL.
- Telemetry is disabled for CI and non-release builds; non-release builds log the required debug message.

Validation so far: `go test ./internal/release ./internal/info ./internal/telemetry ./cmd/flipt` passed. Rechecking after the empty-response guard and reviewing the final diff.
