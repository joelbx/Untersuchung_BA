Implemented the generic fanout buffer in [buffer.go](/app/lib/utils/fanoutbuffer/buffer.go), with independent cursors, ordered overflow storage, per-cursor grace periods, blocking reads, and cleanup. Added focused tests in [buffer_test.go](/app/lib/utils/fanoutbuffer/buffer_test.go).

The package’s race tests and vet check passed. The existing `lib/services` fanout tests also passed.