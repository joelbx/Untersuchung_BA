# Checkpoint

Resolved startup release/update handling in the checked-out repository.

- Added `internal/release/check.go` with `Info`, `Is`, and `Check`. `Is` excludes `dev`, `snapshot`, and `rc` prerelease identifiers; `Check` retrieves and compares the latest release and logs a warning with the error on failure.
- Startup now uses `release.Is(version)` and `release.Check(ctx, version)`, reports status from `release.Info`, and preserves the current version in `info.Flipt`. Added latest release URL to `info.Flipt`.
- Telemetry is disabled in CI and for non-release builds, with the required debug message for non-release builds.
- Added local tests for prerelease classification, update comparison, and failed check handling.

Verification: `GOPROXY=off go test ./internal/release ./cmd/flipt ./internal/info ./internal/telemetry ./internal/server/metadata` exited 0: release and telemetry tests passed; remaining packages had no test files.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); local `find`/`grep` were used. No offline Go tooling check was blocked.
