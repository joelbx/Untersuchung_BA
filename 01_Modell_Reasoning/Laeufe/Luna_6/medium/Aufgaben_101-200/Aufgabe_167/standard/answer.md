Implemented the context-aware `SnapshotSource.Get` interface, updated existing source implementations and test fixtures, and added the OCI filesystem source with configurable polling and digest-based snapshot updates. OCI layer fetching now accepts a `ReadOnlyTarget` and recognizes both Flipt namespace and feature media types.

Focused tests pass: `go test ./internal/storage/fs/... ./internal/oci/...`.

One requirement remains incomplete: local OCI layouts are still fetched through the store’s existing cached target; they are not lazily reopened on every fetch.