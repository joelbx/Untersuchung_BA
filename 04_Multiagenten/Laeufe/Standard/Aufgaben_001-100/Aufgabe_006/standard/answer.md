Implemented the generic fanout buffer in [buffer.go](/app/lib/utils/fanoutbuffer/buffer.go). It supports ordered concurrent cursors, overflow storage with grace period expiry, blocking and nonblocking reads, and cleanup on cursor or buffer closure.

Added focused tests in [buffer_test.go](/app/lib/utils/fanoutbuffer/buffer_test.go). `go test -race ./lib/utils/fanoutbuffer` passes.