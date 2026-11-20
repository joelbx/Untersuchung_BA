# Checkpoint

Task: resolve multi-backend audit event initialization by adding a writer-backed emitter and correcting MultiLog validation/fan-out/close behavior.

Findings: `stdout://` currently constructs `WriterLog`, which does not implement `Emitter`; `MultiLog` stores loggers but does not embed a `MultiEmitter`. The service already parses `AuditEventsURI` as a list and has one call site for `NewMultiLog`.

Changes: added `WriterEmitter` with newline-delimited JSON output and single-owner writer closure; `NewMultiLog` now validates emitter support and embeds a `MultiEmitter`; `stdout://` now uses `NewWriterEmitter`.

Verification: `go test ./lib/events` and `go test ./lib/service` both passed. `git diff --check` passed.
