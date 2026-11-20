# Checkpoint

Task: fix polling goroutine lifecycle across storage backends in `/app`.

Implemented a context-owned `Poller` with a stored `UpdateFunc`, parameterless `Poll()`, and idempotent `io.Closer` shutdown that waits for termination. Git, local, Azure Blob, S3, and OCI stores now retain the poller and expose nil-safe `Close()` methods. Git's immutable hash mode remains poller-free.

Verification: `gofmt` completed, `git diff --check` passed, and `go test ./internal/storage/fs/...` passed for all packages.
