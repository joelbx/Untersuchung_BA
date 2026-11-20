Implemented polling lifecycle management. `Poller.Close()` cancels its context and waits for a running poll loop to finish. Git, local, S3, Azure Blob, and OCI stores retain their poller and expose safe `Close()` methods; stores without an active poller return successfully.

Added `Close()` to the shared `SnapshotStore` interface and delegated it through the storage wrapper.

Verification: `go test ./internal/storage/fs/...` passed, and `git diff --check` reported no issues.