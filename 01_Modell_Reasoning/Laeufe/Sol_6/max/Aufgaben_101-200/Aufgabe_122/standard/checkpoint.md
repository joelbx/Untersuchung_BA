# Progress checkpoint

- Task: add validated `storage.readOnly` configuration, propagate it to UI state and header, and avoid database authentication bootstrap for disabled authentication on non-database storage.
- Initial repository status: clean.
- Inspected configuration, metadata serialization, UI selectors/header, and authentication bootstrap.
- Added `StorageConfig.ReadOnly` as an optional boolean, validation, and the required invalid object-storage fixture.
- Updated UI config types, read-only selector, and storage-aware header badge. Extended the authentication shortcut to object storage and added focused Go tests.
- Database storage now loads without the filesystem experiment flag, while non-database storage still requires it. The default storage type is explicitly database so metadata and UI agree.
- Updated CUE and JSON schemas for the flag and object storage type.
- Relevant Go tests passed: `go test ./internal/config ./internal/cmd ./config ./internal/server/metadata` with network access disabled.
- UI tooling is not installed in this environment (`node`, `npm`, and `tsc` are unavailable); reviewed TypeScript changes statically.
- Final diff review complete; `git diff --check` passed.
