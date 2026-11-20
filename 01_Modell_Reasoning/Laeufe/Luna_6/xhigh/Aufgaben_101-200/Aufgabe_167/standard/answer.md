Implemented OCI backed feature flag storage.

- Added [`internal/storage/fs/oci/source.go`](/app/internal/storage/fs/oci/source.go) with context aware `Get`, digest based snapshot updates, configurable polling, and cancellation aware subscriptions.
- Updated OCI fetching to reopen local layouts on each fetch, support namespace and features layers, decode gzip content, and carry namespace annotations into snapshots.
- Migrated existing snapshot sources and callers to the context aware `Get` signature, and wired OCI storage into server startup.

Verification passed: `go test ./internal/storage/fs/... ./internal/oci ./internal/cmd` and `git diff --check`. The new OCI source package currently has no test files.