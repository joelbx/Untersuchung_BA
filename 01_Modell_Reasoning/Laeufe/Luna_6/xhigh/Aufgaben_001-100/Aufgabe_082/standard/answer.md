Implemented the audit backend fix.

- Added `WriterEmitter` with newline-delimited JSON output and resource closure.
- Updated `NewMultiLog` to validate emitters and fan out events through `MultiEmitter`.
- Switched `stdout://` to `NewWriterEmitter`.

Verification passed: `go test ./lib/events`, `go test ./lib/service`, and `git diff --check`.

Files: [emitter.go](/app/lib/events/emitter.go), [multilog.go](/app/lib/events/multilog.go), [service.go](/app/lib/service/service.go).