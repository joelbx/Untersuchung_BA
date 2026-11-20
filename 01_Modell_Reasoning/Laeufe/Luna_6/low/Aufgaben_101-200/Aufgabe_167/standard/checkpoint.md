# Checkpoint

Implemented context-aware `SnapshotSource.Get(context.Context)` across local, Git, S3, store startup, and test source implementations. Added `internal/storage/fs/oci.Source` with digest-aware snapshot reuse and configurable polling. Updated the OCI store to reopen local OCI layouts for each fetch, accept an explicit ORAS target in `fetchFiles`, and support namespace/features layer media types plus gzip decoding.

Verification: `go test ./internal/oci ./internal/storage/fs/...` passed; `git diff --check` passed. Existing tests cover OCI store fetching and current source implementations; the new OCI source package has no checked-in tests yet.
