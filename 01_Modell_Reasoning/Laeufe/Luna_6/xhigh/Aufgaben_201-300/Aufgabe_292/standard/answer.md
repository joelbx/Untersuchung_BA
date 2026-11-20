Implemented managed polling lifecycle across Git, local, Azure Blob, S3, and OCI stores. The poller now owns a cancellable context, and `Close()` waits for polling to stop, including when called before polling starts. Snapshot stores and the filesystem store wrapper expose `Close()`, and gRPC shutdown closes the store.

Verification passed: `GOPROXY=off go test ./internal/storage/fs/... ./internal/cmd`. `git diff --check` is clean.

Key changes: [poll.go](/app/internal/storage/fs/poll.go), [store.go](/app/internal/storage/fs/store.go), and backend store implementations.