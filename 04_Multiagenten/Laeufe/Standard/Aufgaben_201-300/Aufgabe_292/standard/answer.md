Polling now has a managed lifecycle. The poller owns its context and update callback, and `Close()` cancels polling and waits for the goroutine to exit. Git, local, Azure Blob, S3, and OCI snapshot stores now expose `Close()`; it safely returns when no poller is active.

Added a test for closing during an update. `go test ./internal/storage/fs/...` passes.