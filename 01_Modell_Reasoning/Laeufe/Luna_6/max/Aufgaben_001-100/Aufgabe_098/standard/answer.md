Telemetry schema version is now `1.3`. The payload includes `audit.sinks` with the enabled `log` and/or `webhook` sinks, and omits `audit` when neither is enabled. Existing telemetry fields retain their behavior.

Added coverage for each sink combination in [telemetry_test.go](/app/internal/telemetry/telemetry_test.go); implementation is in [telemetry.go](/app/internal/telemetry/telemetry.go).

Verification passed: `go test ./internal/telemetry` and `git diff --check`.