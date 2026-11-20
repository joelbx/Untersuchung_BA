Implemented the generic fanout buffer in [buffer.go](/app/lib/utils/fanoutbuffer/buffer.go), with independent cursors, ordered reads, overflow and grace period handling, and cleanup of consumed items. Added tests in [buffer_test.go](/app/lib/utils/fanoutbuffer/buffer_test.go).

Verification passed: the package race test, `go vet`, and the existing `lib/services` Fanout tests.