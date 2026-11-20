# Checkpoint

Implemented `internal/release.Info`, `release.Check`, and `release.Is`; startup now consumes release metadata, reports the update result according to the configured output mode, exposes the latest URL in `info.Flipt`, and disables telemetry for non-release builds and CI.

Verification: `go test ./internal/release ./internal/info ./cmd/flipt` and `git diff --check` succeeded. The focused packages currently have no test files.
