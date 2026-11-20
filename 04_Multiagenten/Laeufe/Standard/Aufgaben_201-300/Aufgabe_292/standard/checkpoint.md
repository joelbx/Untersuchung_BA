# Checkpoint

Task: stop storage polling goroutines when SnapshotStore.Close is called.
Status: implemented and verified with go test ./internal/storage/fs/...; all packages pass.
