# Checkpoint

Task: Add audit sink configuration to anonymous telemetry and update schema version to 1.3.

Completed: Telemetry includes `flipt.audit.sinks` for enabled log file and webhook sinks and omits `audit` when neither is enabled. Existing telemetry fields remain unchanged. Added table cases for disabled, log, webhook, and both; updated version assertions.

Verification: `go test ./internal/telemetry` passed. `git diff --check` passed.
