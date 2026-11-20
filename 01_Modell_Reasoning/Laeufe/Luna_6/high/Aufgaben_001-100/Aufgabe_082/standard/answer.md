Implemented the audit backend fix.

- Added `WriterEmitter` with JSON-lines output, trace-wrapped write errors, and aggregated close errors.
- Updated `NewMultiLog` to validate emitters, return `trace.BadParameter` for invalid loggers, and fan out events through its embedded `MultiEmitter`.
- Switched `stdout://` to `NewWriterEmitter` and propagated `NewMultiLog` errors.

Verification passed: `go test ./lib/events ./lib/service` and `git diff --check`.