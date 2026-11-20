# Checkpoint

Task: Manage polling lifecycle across storage backends with test-first changes.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using find and grep.

Implemented poller ownership and shutdown in Git, local, OCI, S3, Azure Blob stores. The poller now stores its update callback and derived context; `Close` cancels and joins its worker. Added a poller regression test and no-active-polling Close tests for each store.

RED: `GOPROXY=off go test ./internal/storage/fs -run '^TestPollerCloseWaitsForUpdateAndStopsFutureUpdates$' -count=1` failed to compile as expected because NewPoller/Poll signatures and Close were missing. `GOPROXY=off go test ./internal/storage/fs/local -run '^TestSnapshotStoreCloseWithoutPolling$' -count=1` failed to compile as expected because Close was missing (and old poller API no longer matched).

GREEN: `GOPROXY=off go test ./internal/storage/fs ./internal/storage/fs/local ./internal/storage/fs/git ./internal/storage/fs/oci ./internal/storage/fs/object/s3 ./internal/storage/fs/object/azblob` passed.

Full suite command `GOPROXY=off go test ./...` is still running.

Full suite `GOPROXY=off go test ./...` completed with exit 1. Changed storage/fs packages passed. Unrelated failures:
- `go.flipt.io/flipt/internal/cache/redis`: `TestSet`, `TestGet`, `TestDelete` could not connect to Docker daemon at unix:///var/run/docker.sock.
- `go.flipt.io/flipt/internal/gitfs`: `Test_FS_Submodule` remote Git fetch returned `Forbidden` for https://github.com/flipt-io/flipt-gitops-test.git/info/refs?service=git-upload-pack.
These integration dependencies are unavailable here; their outcomes remain unverified.

Race check `GOPROXY=off go test -race ./internal/storage/fs -run '^TestPollerCloseWaitsForUpdateAndStopsFutureUpdates$' -count=1` passed.
