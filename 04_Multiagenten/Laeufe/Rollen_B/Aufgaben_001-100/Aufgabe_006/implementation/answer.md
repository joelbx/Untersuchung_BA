Implemented the generic fanout buffer in [buffer.go](/app/lib/utils/fanoutbuffer/buffer.go). It supports independent ordered cursors, ring and overflow storage, grace period expiry, blocking reads, and cleanup when cursors advance or close.

Added focused tests in [buffer_test.go](/app/lib/utils/fanoutbuffer/buffer_test.go). Verification passed: `go test -race -count=10 ./lib/utils/fanoutbuffer`.