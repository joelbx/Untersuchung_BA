Implemented the audit backend fix.

- Added `WriterEmitter` and `NewWriterEmitter` to write newline-delimited JSON events and aggregate close errors.
- Updated `NewMultiLog` to validate that each logger implements `Emitter` and to fan events out through an embedded `MultiEmitter`.
- Changed the `stdout://` backend to use `WriterEmitter` and propagated `NewMultiLog` errors.

Verification passed: `go test ./lib/events ./lib/service` and `git diff --check`.