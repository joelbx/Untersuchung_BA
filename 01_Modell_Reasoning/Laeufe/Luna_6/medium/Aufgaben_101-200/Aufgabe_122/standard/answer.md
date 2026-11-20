Implemented the storage read-only configuration and UI updates.

- Added optional `StorageConfig.ReadOnly` with validation that rejects it for non-database storage, plus the requested invalid YAML fixture.
- Updated authentication bootstrap to skip database connections when authentication is disabled and storage is not database-backed.
- Added `IStorage.readOnly`, the `OBJECT` storage type, and exported `selectConfig`. Read-only state now uses `config.storage.readOnly`, defaulting to true for non-database storage.
- Updated the header to show the “Read-Only” badge with an icon for the active storage backend.

**Verification:** `go test ./internal/config ./internal/cmd` passed. UI tests could not run because `npm` is unavailable.