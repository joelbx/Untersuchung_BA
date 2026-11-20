Fixed the auth service audit backend crash. `MultiLog` now validates its loggers and fans out audit events through an embedded `MultiEmitter`. The `stdout://` backend now uses the new `WriterEmitter`, which writes newline-delimited JSON events and closes its resources.

Verification passed: `go test ./lib/events ./lib/service` and `git diff --check`.