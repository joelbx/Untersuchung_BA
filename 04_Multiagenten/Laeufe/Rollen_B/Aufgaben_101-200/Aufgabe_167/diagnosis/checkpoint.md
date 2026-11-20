Progress: Fault localization complete from repository code and existing tests. No project source or tests changed.

Findings:
- internal/storage/fs/oci/source.go does not exist. SnapshotSource.Get is context-free in internal/storage/fs/store.go; existing local/git/s3 sources, Store.NewStore, and test call sites use Get().
- internal/oci/file.go Store.Fetch caches the oras OCI layout target and in-memory destination on NewStore. Local tag/index changes made externally can therefore remain invisible. Fetch has IfNoMatch digest support, but fetchFiles uses s.store directly and accepts only namespace media type plus plain json/yaml/yml encoding.
- Existing OCI tests cover initial local fetch, unchanged IfNoMatch, invalid media/encoding. They do not cover retagging after Store creation, source subscription, gzip, or namespace annotation handling. SnapshotFromFiles consumes fs.File; its YAML parser uses the document namespace or default, so layer namespace annotation is not currently applied by the OCI wrapper.
- internal/cmd/grpc.go has no OCIStorageType case despite configuration recognizing it; if end-to-end configured OCI storage is required, wiring there is needed.

Verification: GOPROXY=off GOSUMDB=off go test ./internal/oci ./internal/storage/fs/... passed. This only establishes the existing baseline; missing behaviors are untested.
