Implemented the generic fanout buffer in [buffer.go](/app/lib/utils/fanoutbuffer/buffer.go), with independent ordered cursors, ring and overflow storage, grace period errors, blocking reads, and cleanup on close. Added focused tests in [buffer_test.go](/app/lib/utils/fanoutbuffer/buffer_test.go).

The package tests passed with the race detector, and `git diff --check` passed.