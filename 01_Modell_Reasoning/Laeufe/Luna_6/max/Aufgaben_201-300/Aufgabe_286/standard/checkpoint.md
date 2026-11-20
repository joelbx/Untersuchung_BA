# Checkpoint

Issue: Separate release/update startup concerns, recognize prerelease builds, report update status, and gate telemetry by CI/release status.

Completed:
- Added `internal/release` with semantic release detection and the default GitHub release lookup. Lookup and parsing failures are logged as warnings and returned for startup to handle without terminating.
- Startup now uses `release.Is` and `release.Check`, reports current/latest version and the latest URL in console or configured logger output, and passes the metadata to `info.Flipt`.
- Added the latest version URL to `info.Flipt` and disabled telemetry for CI (`true` or `1`) and non-release builds with the required debug message.

Verification completed with module downloads disabled:
- `go test ./cmd/flipt ./internal/info ./internal/release ./internal/telemetry`
- `git diff --check`
