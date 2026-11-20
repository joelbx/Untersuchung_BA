Implemented the startup release/update separation.

- Added [`internal/release/check.go`](/app/internal/release/check.go) for release detection and update lookup. Prerelease builds are excluded, and failed checks log a warning while allowing startup to continue.
- Updated [`main.go`](/app/cmd/flipt/main.go) to use the release info for console or logger status messages and to disable telemetry for CI and non-release builds.
- Added the latest release URL to [`info.Flipt`](/app/internal/info/flipt.go).

Verification passed with module downloads disabled: `go test ./cmd/flipt ./internal/info ./internal/release ./internal/telemetry` and `git diff --check`. Telemetry tests passed; the other packages compiled and have no test files.