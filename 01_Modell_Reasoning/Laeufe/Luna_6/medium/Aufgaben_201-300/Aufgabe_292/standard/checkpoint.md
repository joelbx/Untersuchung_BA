# Checkpoint

Implemented cancellable polling in `internal/storage/fs.Poller`: it stores the parent-derived context and update callback, exposes parameterless `Poll()`, implements `io.Closer`, and waits for loop termination on close. Git, local, Azure Blob, S3, and OCI snapshot stores retain their poller and expose an idempotent safe `Close()` (nil poller is a no-op).

Validation: `go test ./internal/storage/fs/...` passed; `git diff --check` passed.
