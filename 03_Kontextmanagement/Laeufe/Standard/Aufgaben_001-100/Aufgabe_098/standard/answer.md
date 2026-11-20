Updated anonymous telemetry to version `1.3`. The payload now includes `flipt.audit.sinks` with `log`, `webhook`, or both when those sinks are enabled, and omits `audit` when neither is enabled. Existing telemetry fields remain unchanged.

Added coverage for all sink combinations. `go test ./internal/telemetry` and `git diff --check` passed.