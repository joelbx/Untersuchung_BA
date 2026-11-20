Added OCI-backed feature flag storage in [source.go](/app/internal/storage/fs/oci/source.go). It polls by digest, reopens local OCI layouts on each fetch to detect external changes, and publishes snapshots only when content changes. The OCI fetch code now handles annotated namespace and features layers, gzip content, and remote registries. OCI storage is wired into the server with a configurable 30-second polling default. `SnapshotSource.Get` and its existing callers now use context.

I delegated the interface migration, OCI fetch changes, and runtime configuration work to three agents, then integrated and reviewed their edits.

Verification passed: the OCI, filesystem storage, config, and command package tests; the OCI source race test; and `git diff --check`.