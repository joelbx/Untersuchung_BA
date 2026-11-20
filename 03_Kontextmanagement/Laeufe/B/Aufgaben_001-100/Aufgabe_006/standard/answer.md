Implemented the generic fanout buffer in [buffer.go](/app/lib/utils/fanoutbuffer/buffer.go), with concurrent cursors, ordered reads, overflow handling, grace period errors, and cleanup. Added focused tests.

Validation passed: `go test -race ./lib/utils/fanoutbuffer` and the existing `TestFanout` tests in `lib/services`.