Implemented the generic fanout buffer in [buffer.go](/app/lib/fanoutbuffer/buffer.go), including configurable defaults, concurrent cursors, blocking and nonblocking reads, grace period errors, close handling, notifications, and cleanup of consumed entries.

Verified with `go test ./lib/fanoutbuffer`; the package compiles and has no existing test files.