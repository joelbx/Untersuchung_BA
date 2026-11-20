Implemented cancellable polling with a stored `UpdateFunc`. `Poller.Close()` cancels its context and waits for polling to stop. Git, local, Azure Blob, S3, and OCI snapshot stores now expose `Close()`; it is a no-op when no poller is active.

Verification passed: `go test ./internal/storage/fs/...` and `git diff --check`.

Changed: [poll.go](/app/internal/storage/fs/poll.go), [git/store.go](/app/internal/storage/fs/git/store.go), [local/store.go](/app/internal/storage/fs/local/store.go), [azblob/store.go](/app/internal/storage/fs/object/azblob/store.go), [s3/store.go](/app/internal/storage/fs/object/s3/store.go), [oci/store.go](/app/internal/storage/fs/oci/store.go).