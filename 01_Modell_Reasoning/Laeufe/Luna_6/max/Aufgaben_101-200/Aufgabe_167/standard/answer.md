Implemented OCI-backed filesystem snapshots in [source.go](/app/internal/storage/fs/oci/source.go), including digest-based refreshes and change-only subscriptions. Local OCI layouts are reopened on each fetch; namespace annotations, supported layer types, gzip encoding, and manifest creation times are carried into snapshots. OCI configuration is now wired into the server.

Updated `SnapshotSource.Get` and its implementations to accept a context, including passing it through S3 object reads.

Verification passed: `go test ./internal/storage/fs/... ./internal/oci ./internal/s3fs ./internal/cmd` and `git diff --check`. The new OCI source package has no existing tests.