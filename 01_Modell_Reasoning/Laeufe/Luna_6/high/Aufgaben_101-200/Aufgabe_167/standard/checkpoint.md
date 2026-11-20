# Checkpoint

Task: Add OCI-backed filesystem snapshot source support and make snapshot reads context-aware.

Completed:
- Updated `SnapshotSource.Get` and local, Git, S3, and test source implementations/callers to accept a context.
- Added `internal/storage/fs/oci.Source` with digest-based `IfNoMatch` fetches, snapshot caching, polling, and context-aware channel sends.
- Reopened local OCI layouts on every fetch and used a fresh in-memory copy target; added support for feature and namespace layer types, namespace annotations, and gzip encoded layer data.
- Wired OCI storage configuration into server store construction.

Verification in progress: `go test ./internal/storage/fs/... ./internal/oci ./internal/cmd`.

Verification complete: `go test ./internal/storage/fs/... ./internal/oci ./internal/cmd` passed. `git diff --check` passed.
