Implemented poller lifecycle management across Git, local filesystem, Azure Blob, S3, and OCI stores. `Poller.Close()` cancels its context and waits for the polling loop to finish; each store exposes a safe `Close()` that does nothing when no poller is active.

`go test ./internal/storage/fs/...` and `git diff --check` passed.