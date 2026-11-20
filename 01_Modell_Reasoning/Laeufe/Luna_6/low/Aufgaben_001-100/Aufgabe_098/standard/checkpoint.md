# Checkpoint

Task: Include enabled audit sinks in anonymous telemetry, bump telemetry version to 1.3, and omit audit data when no sink is enabled.

Implemented in `internal/telemetry/telemetry.go`: added optional `flipt.audit.sinks`, populated from configured log and webhook enablement, and updated schema version to 1.3. Extended `internal/telemetry/telemetry_test.go` for log, webhook, both sinks, existing omission behavior, and schema version.

Verification: `go test ./internal/telemetry` passes. `git diff --check` passes.
