# Checkpoint

Implemented the audit event backend integration:

- Added `WriterEmitter` and `NewWriterEmitter` to write newline-delimited JSON events and aggregate close errors.
- Updated `NewMultiLog` to validate every logger implements `Emitter`, return a bad-parameter error for invalid loggers, and embed a fan-out `MultiEmitter`.
- Changed stdout backend initialization to use `WriterEmitter` and propagated `NewMultiLog` errors.

Verification: `go test ./lib/events ./lib/service` passed; `git diff --check` passed.
