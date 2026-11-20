Polling now has an owned lifecycle. The Git, local, S3, Azure Blob, and OCI snapshot stores retain their poller and expose `Close()`; closing a store cancels polling and waits for the goroutine to exit. A store with no active poller closes safely.

Added a test that checks `Close()` waits for an in-progress update. `go test ./internal/storage/fs/...` and `git diff --check` pass.