Implemented the generic fanout buffer in [buffer.go](/app/lib/utils/fanoutbuffer/buffer.go). It supports independent ordered cursors, ring and overflow storage, grace period errors, blocking reads, and cleanup on cursor or buffer close.

Verification passed: the new package’s tests under the race detector and the existing `lib/services` fanout tests.