Implemented terminal restoration for canceled password reads and `Close`, and added `NotifyExit` to close the global stdin reader. Deadline expiration returns an empty result with a `context.DeadlineExceeded` error.

`go test ./lib/utils/prompt` passes.