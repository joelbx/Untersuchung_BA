# Checkpoint

Implemented the release/update separation and startup behavior in `internal/release`, `cmd/flipt`, and `internal/info`. Release detection excludes `dev`, `-snapshot`, `-rc`, and semantic prereleases. Update checks return current/latest version, update availability, and the latest release URL; failures emit the `checking for updates` warning and startup continues. Startup reports status through console colors or the configured logger, exposes metadata in `info.Flipt`, and disables telemetry for CI and non-release builds.

Validation completed:
- `go test ./internal/release ./internal/info ./cmd/flipt` (passed; packages without tests compiled)
- `go test ./internal/telemetry` (passed)
- `git diff --check` (passed)
