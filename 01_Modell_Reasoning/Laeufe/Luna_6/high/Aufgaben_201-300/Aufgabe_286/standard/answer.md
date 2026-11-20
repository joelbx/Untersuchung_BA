Implemented release handling in [internal/release/check.go](/app/internal/release/check.go), startup reporting in [main.go](/app/cmd/flipt/main.go), and latest release URL metadata in [flipt.go](/app/internal/info/flipt.go).

Prerelease builds (`dev`, `-snapshot`, `-rc`, and semantic prereleases) are excluded from release detection. Startup uses `release.Check` for update status, reports versions through the configured output mode, and disables telemetry for CI or non-release builds. Update check failures log a warning and do not stop startup.

Validation passed: `go test ./internal/release ./internal/info ./cmd/flipt`, `go test ./internal/telemetry`, and `git diff --check`.