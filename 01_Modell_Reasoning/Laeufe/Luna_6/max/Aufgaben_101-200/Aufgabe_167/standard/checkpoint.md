# Checkpoint

Task: Add OCI-backed filesystem snapshot source support and make snapshot retrieval context-aware.

Completed:
- Added a context parameter to `SnapshotSource.Get`, updated local, Git, S3, and OCI implementations, and updated callers.
- Added `internal/storage/fs/oci.Source` with a 30 second default polling interval, digest-based snapshot caching, cancellable change-only subscriptions, and structured logging.
- Updated OCI fetching to reopen local layouts for every fetch, honor `IfNoMatch`, accept namespace and features layers, validate encodings, decompress gzip payloads, and carry namespace and manifest creation metadata into snapshots.
- Connected OCI storage configuration to the filesystem store and passed request contexts through S3 object reads.

Verification:
- `go test ./internal/storage/fs/... ./internal/oci ./internal/s3fs ./internal/cmd` passed.
- `git diff --check` passed.
