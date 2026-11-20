# Checkpoint

Task: add optional audit sink configuration to anonymous telemetry and bump telemetry schema version to 1.3.

Progress: implemented the optional `flipt.audit.sinks` field from configured log and webhook sink enable flags; updated telemetry schema expectations and added tests for log, webhook, both sinks, and omission when no sinks are enabled.

Validation: `go test ./internal/telemetry` passed. Formatting applied with `gofmt`. Restored the test-generated `go.work.sum` changes.
