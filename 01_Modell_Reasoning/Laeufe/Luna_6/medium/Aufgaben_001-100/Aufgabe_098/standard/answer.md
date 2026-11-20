Implemented audit sink reporting in [telemetry.go](/app/internal/telemetry/telemetry.go): the telemetry schema version is now `1.3`, and the payload includes `audit: {"sinks": [...]}` for enabled log and webhook sinks. The audit field is omitted when neither sink is enabled.

Added coverage for log, webhook, both sinks, and the existing no-sink cases in [telemetry_test.go](/app/internal/telemetry/telemetry_test.go).

Verified with `go test ./internal/telemetry` and `git diff --check`; both pass.