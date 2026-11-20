Updated anonymous telemetry to version `1.3`. When audit sinks are enabled, the payload includes `audit.sinks` with `log`, `webhook`, or both; when neither is enabled, it omits `audit`.

Added coverage for all sink combinations in [telemetry_test.go](/app/internal/telemetry/telemetry_test.go). `go test ./internal/telemetry` and `git diff --check` passed.