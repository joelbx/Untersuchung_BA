# Polling lifecycle fix

Status: Complete.

Changes: Poller owns an update callback, cancelable context, and completion channel. All five SnapshotStores retain and close their poller. The existing SnapshotStore interface, fs.Store wrapper, and gRPC shutdown expose/forward Close. Existing backend tests close their stores during cleanup. Poller lifecycle tests cover in-flight work, repeated Close, Close before Poll, and parent cancellation.

Validation: gofmt and git diff --check passed. Offline `go test -count=1 ./internal/storage/fs/... ./internal/cmd` passed. Offline `go test -race ./internal/storage/fs ./internal/storage/fs/local` passed.
