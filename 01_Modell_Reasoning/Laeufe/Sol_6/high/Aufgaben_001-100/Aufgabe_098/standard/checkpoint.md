# Checkpoint

Task: include enabled audit sinks in anonymous telemetry and update schema version to 1.3.

Status: implemented `flipt.audit.sinks` for enabled log and webhook sinks, omitted when neither is enabled; updated telemetry version to 1.3. Added existing ping test cases for disabled, log only, webhook only, and both. `GOPROXY=off GOSUMDB=off go test ./internal/telemetry` passed. Restored incidental `go.work.sum` change from the test run.
