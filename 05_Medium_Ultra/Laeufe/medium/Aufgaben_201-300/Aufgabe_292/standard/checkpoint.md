Task: manage polling goroutine lifecycle across filesystem SnapshotStores.
Status: Complete. Poller owns context, cancellation, and completion tracking. Git, local, OCI, S3, and Azure Blob stores retain and close their pollers. Added poller lifecycle and local store close tests. `go test ./internal/storage/fs/...` and `git diff --check` pass.
