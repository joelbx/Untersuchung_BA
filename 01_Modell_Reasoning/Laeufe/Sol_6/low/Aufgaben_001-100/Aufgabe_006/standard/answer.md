Implemented `lib/utils/fanoutbuffer` with a generic concurrent buffer, independent cursors, overflow retention, grace period expiry, blocking and nonblocking reads, and close handling.

Added tests for ordering, overflow, grace expiry, wakeups, and closed state. `go test -race ./lib/utils/fanoutbuffer` passes.