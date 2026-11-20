Implemented the release and startup changes.

- Added [internal/release/check.go](/app/internal/release/check.go) for release detection and update checks. Check failures log a warning and return control to startup.
- Updated [main.go](/app/cmd/flipt/main.go) to report update status in the configured output mode and disable telemetry for CI or non-release builds.
- Added the latest release URL to [info.Flipt](/app/internal/info/flipt.go) metadata.
- Recorded progress in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).

`go test ./internal/release ./internal/info ./internal/telemetry ./cmd/flipt` passed. The release, info, and command packages have no existing tests; telemetry tests passed.