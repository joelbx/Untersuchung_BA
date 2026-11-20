# Checkpoint

Task: implement OCI-backed filesystem snapshot source support and migrate SnapshotSource.Get to context-aware calls.

Progress: implemented the OCI-backed `SnapshotSource`, migrated existing snapshot sources to context-aware `Get` methods, and wired OCI storage into server construction. Local OCI layouts are reopened on each fetch; layer media types, namespace annotations, gzip encoding, and manifest creation timestamps are handled when building snapshots.

Verification: `go test ./internal/storage/fs/... ./internal/oci` passed. `go test ./internal/cmd` passed. `git diff --check` passed.
