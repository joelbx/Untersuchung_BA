Implemented terminal restoration and shutdown handling.

- `ContextReader` restores terminal state on abandoned or interrupted password reads, and `Close` attempts restoration before closing. Canceled reads return empty results with the context error and transition to clean state when restoration succeeds. [context_reader.go](/app/lib/utils/prompt/context_reader.go:230)
- Added `NotifyExit` to close the global stdin reader, and call it when `tsh` finishes running. [stdin.go](/app/lib/utils/prompt/stdin.go:58) [tsh.go](/app/tool/tsh/tsh.go:395)

Validation: `go test ./lib/utils/prompt` and `git diff --check` pass. `go test ./tool/tsh` fails in `TestExportingTraces`: its exporter connection to `grpc://0.0.0.0:33177` times out, followed by tracing scope assertion failures.