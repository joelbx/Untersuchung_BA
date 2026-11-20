Updated telemetry to version `1.3`. The payload now includes `flipt.audit.sinks` with the enabled `log` and `webhook` sinks, and omits `audit` when neither is enabled. The existing telemetry fields are unchanged.

Added test coverage for all four sink combinations. `go test ./internal/telemetry` passed.