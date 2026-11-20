Implemented terminal restoration for abandoned password reads and `Close`, including propagation of restoration errors. Added `NotifyExit` to close the global stdin reader.

`go test ./lib/utils/prompt` passes.

Changes: [context_reader.go](/app/lib/utils/prompt/context_reader.go:220), [stdin.go](/app/lib/utils/prompt/stdin.go:56).