# Checkpoint

Implemented optional audit telemetry in `internal/telemetry/telemetry.go`: the payload reports `audit.sinks` with enabled `log` and/or `webhook` values, and omits `audit` when neither sink is enabled. Updated telemetry schema version to 1.3.

Updated existing telemetry tests with coverage for each enabled sink combination and the new schema version. Validation: `go test ./internal/telemetry` passed.
