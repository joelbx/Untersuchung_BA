# Checkpoint

Implemented lifecycle management for storage polling.

- `Poller` owns a derived context, callback, cancellation function, and completion signal; `Close()` cancels and waits for a running poll loop.
- Git, local, S3, Azure Blob, and OCI snapshot stores retain their poller and expose idempotent `Close()` methods. Stores without an active poller return successfully.
- Added `Close()` to the shared `SnapshotStore` interface and delegated it through the storage wrapper.
- Verified with `go test ./internal/storage/fs/...` (all packages passed) and `git diff --check`.
