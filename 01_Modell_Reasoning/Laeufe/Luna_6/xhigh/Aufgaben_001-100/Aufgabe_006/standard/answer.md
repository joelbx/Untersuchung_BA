Implemented [buffer.go](/app/lib/services/fanoutbuffer/buffer.go) with configurable defaults, ring and overflow storage, concurrent cursors, grace-period expiration, blocking and non-blocking reads, cleanup, and close notifications.

Verification passed: `go test ./lib/services/fanoutbuffer` and `go test ./lib/services -run 'Test(Fanout|UnsupportedKind)' -count=1`.