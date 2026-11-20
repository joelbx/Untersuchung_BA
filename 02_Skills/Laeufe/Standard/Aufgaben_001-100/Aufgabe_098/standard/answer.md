Updated anonymous telemetry to version `1.3`. The payload now includes `flipt.audit.sinks` with `"log"`, `"webhook"`, or both when those sinks are enabled, and omits `audit` when neither is enabled.

Added coverage for all four sink combinations. `go test ./internal/config ./internal/telemetry` and `git diff --check` passed.