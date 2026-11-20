# Checkpoint

Task: resolve polling goroutine lifecycle management across storage backends in `/app`.

Completed:
- Added `UpdateFunc` and a poller that owns a child context, cancellation, worker completion tracking, and an `io.Closer`-compatible `Close()` that waits for termination. `Close()` is safe before polling starts.
- Added `Close() error` to the existing `SnapshotStore` interface; Git, local, Azure Blob, S3, and OCI stores retain their poller and implement nil-poller no-op close behavior.
- Added close delegation to the filesystem `Store` wrapper and registered it during gRPC server shutdown.
- Updated the existing snapshot-store mock to satisfy the interface.

Verification: `GOPROXY=off go test ./internal/storage/fs/... ./internal/cmd` passed. `git diff --check` is clean.
