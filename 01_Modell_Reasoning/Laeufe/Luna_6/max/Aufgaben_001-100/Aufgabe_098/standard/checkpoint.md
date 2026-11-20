# Checkpoint

- Task: include enabled audit sinks in anonymous telemetry, with schema version 1.3.
- Implementation: added optional `flipt.audit.sinks`, populated from the configured log file and webhook enablement flags. The field is omitted when neither sink is enabled.
- Coverage: telemetry tests exercise log only, webhook only, both sinks, and the existing no-sink cases; telemetry version expectations now use 1.3.
- Verification: `go test ./internal/telemetry` passed; `git diff --check` passed.
- The test run added workspace checksum entries; `go.work.sum` has been restored to its initially clean contents.
