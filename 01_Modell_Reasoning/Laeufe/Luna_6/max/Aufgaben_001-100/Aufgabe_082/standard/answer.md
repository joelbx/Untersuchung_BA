Implemented the audit backend fix:

- Added `WriterEmitter` for newline-delimited JSON output and aggregated close handling in [emitter.go](/app/lib/events/emitter.go:206).
- Updated `NewMultiLog` to validate emitters and fan out events; closing it now aggregates errors from its backends in [multilog.go](/app/lib/events/multilog.go:29).
- Switched the stdout backend to `WriterEmitter` and handled `NewMultiLog` errors in [service.go](/app/lib/service/service.go:905).

Both relevant test commands passed: `go test ./lib/events` and `go test ./lib/service -check.f TestInitExternalLog`.