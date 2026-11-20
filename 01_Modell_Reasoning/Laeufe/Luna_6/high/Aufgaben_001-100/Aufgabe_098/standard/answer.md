Implemented optional `audit.sinks` telemetry reporting for enabled log and webhook sinks, and updated the telemetry schema version to `1.3`. When neither sink is enabled, the audit field is omitted.

Updated the existing telemetry tests to cover log, webhook, both sinks, and the new version. `go test ./internal/telemetry` passes.