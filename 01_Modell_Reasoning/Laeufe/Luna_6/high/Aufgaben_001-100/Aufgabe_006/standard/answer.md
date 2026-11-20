Implemented the generic fanout buffer in [buffer.go](/app/fanoutbuffer/buffer.go), with configurable defaults, a fixed ring and overflow backlog, concurrent cursors, blocking and non-blocking reads, grace period errors, cleanup, and close signaling.

Verification passed: `go test ./fanoutbuffer` and `go test ./lib/services`. The new package has no checked-in tests.