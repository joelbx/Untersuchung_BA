Implemented terminal restoration for canceled password reads and `Close`, added `NotifyExit` to close the global stdin reader, and preserved context timeout errors with an empty result.

Validation: `go test ./lib/utils/prompt` passed.

Changed [context_reader.go](/app/lib/utils/prompt/context_reader.go) and [stdin.go](/app/lib/utils/prompt/stdin.go).