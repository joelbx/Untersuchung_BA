Implemented OCI-backed filesystem snapshots and updated `SnapshotSource.Get` to accept a context across existing implementations and callers.

The OCI source reuses snapshots when the digest is unchanged, polls every 30 seconds by default, and checks local OCI layouts through a fresh store handle on each fetch. OCI fetching now accepts an explicit ORAS target and handles namespace and feature layers with gzip decoding.

Verification passed: `go test ./internal/oci ./internal/storage/fs/...` and `git diff --check`. The new OCI source package has no dedicated checked-in tests yet. Progress is recorded in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).