Implemented `WriterEmitter` with JSON line output and aggregated close errors, added `MultiLog` emitter validation and fanout, and switched `stdout://` to use `WriterEmitter`.

Verification passed: `go test ./lib/events ./lib/service` and `git diff --check`.