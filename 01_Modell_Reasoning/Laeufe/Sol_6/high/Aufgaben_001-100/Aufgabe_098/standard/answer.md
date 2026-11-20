Updated anonymous telemetry to version `1.3`. The payload now includes `flipt.audit.sinks` with `"log"` and/or `"webhook"` when those sinks are enabled, and omits `audit` when neither is enabled. Existing telemetry fields retain their structure and behavior.

Added tests for all four sink combinations. `go test ./internal/telemetry` passed, and `git diff --check` found no whitespace issues.