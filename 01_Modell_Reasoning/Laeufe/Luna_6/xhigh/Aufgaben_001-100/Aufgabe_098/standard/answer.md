Implemented audit telemetry with schema version `1.3`. The payload now includes `flipt.audit.sinks` for enabled log and webhook sinks, and omits `audit` when neither is enabled. Existing telemetry fields retain their behavior.

Added coverage for log only, webhook only, both sinks, and omission when no sinks are enabled. Updated the checkpoint at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).

Validation: `go test ./internal/telemetry` passed; `git diff --check` passed.