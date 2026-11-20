# Checkpoint

Task: Add enabled audit sinks to anonymous telemetry and update schema version to 1.3.
Status: Complete. Telemetry includes `flipt.audit.sinks` only when log or webhook sink is enabled; schema version is 1.3.
Verification: `GOPROXY=off GOSUMDB=off go test ./internal/telemetry` passed. `git diff --check` passed.
Changed files: `internal/telemetry/telemetry.go`, `internal/telemetry/telemetry_test.go`.
