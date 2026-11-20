Implemented release detection and update handling.

- Added `release.Is` to exclude `dev`, `snapshot`, and `rc` prerelease versions.
- Added `release.Check` to fetch and compare versions, returning current/latest versions, the latest URL, and update status. Lookup failures log a warning and do not stop startup.
- Updated startup reporting for console and configured logger output, and exposed the latest version URL in `info.Flipt`.
- Telemetry is disabled for CI and non-release builds; non-release builds log the required debug message.

Verification passed: `go test ./internal/release ./internal/info ./cmd/flipt` and `git diff --check`. These packages currently have no test files.