# Checkpoint

Issue implementation is complete.

Changes:
- Added optional pointer-backed `StorageConfig.ReadOnly`, preserving omitted versus explicit `false`, and validation with the required error text for non-database storage.
- Kept database `readOnly` available when experimental filesystem storage is disabled, while preserving the filesystem-storage gate.
- Added the requested invalid object-storage fixture and a database read-only fixture; registered both in config loading tests.
- Updated authentication bootstrap to avoid database setup for configured non-database storage when auth is disabled, while treating an omitted storage type as the database default.
- Added frontend `IStorage.readOnly`, `StorageType.OBJECT`, exported `selectConfig`, and read-only fallback derived from config with database as the default storage type.
- Updated the header with backend-specific icons and a “Read-Only” badge that includes the active backend icon.

Validation passed: `go test ./internal/config ./internal/cmd`; `git diff --check`.
The UI test/build toolchain is not installed locally, and dependencies were not downloaded.
