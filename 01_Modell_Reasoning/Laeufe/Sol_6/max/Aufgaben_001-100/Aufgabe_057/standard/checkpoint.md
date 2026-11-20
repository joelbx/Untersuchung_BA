# Checkpoint

- Task: implement YAML-native variant attachment import/export in `/app`.
- Repository baseline has no `internal/ext` directory; inspect existing CLI and storage interfaces before adding the package.
- Implemented `internal/ext` document model, exporter, and importer; CLI now calls them. Initial compilation of `./internal/ext` and `./cmd/flipt` passes.
- Added YAML fixtures and SQLite-backed round-trip, no-attachment, nested-key, and pagination tests. JSON numbers retain precision; explicit null attachments remain distinct from omitted attachments; empty string attachments are skipped.
- Verification: `go test ./...` passed, and a built CLI imported then exported the fixture byte-for-byte.
