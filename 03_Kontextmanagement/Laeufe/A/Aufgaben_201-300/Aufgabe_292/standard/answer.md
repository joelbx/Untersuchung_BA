Polling now stops when `Close()` is called. The poller cancels its internal context and waits for its goroutine to exit; Git, local, OCI, S3, and Azure Blob snapshot stores retain and close their pollers. Closing a store without active polling is a safe no-op.

Added lifecycle tests. `go test ./internal/storage/fs/...` passes.