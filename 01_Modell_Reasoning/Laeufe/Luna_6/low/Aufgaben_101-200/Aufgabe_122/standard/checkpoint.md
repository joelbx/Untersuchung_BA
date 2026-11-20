# Checkpoint

Implemented:
- Added optional `StorageConfig.ReadOnly` and validation that rejects any explicitly configured value outside database storage.
- Added the requested invalid object storage fixture and config test case.
- Updated authentication bootstrap to skip database access whenever auth is disabled and the configured storage type is non-database.
- Added `IStorage.readOnly`, the `OBJECT` storage enum, exported `selectConfig`, and config-driven readonly fallback in `selectReadonly`.
- Added a visible storage backend icon and retained the Read-Only badge in the header.

Verification underway: `go test ./internal/config` passed. `go test ./internal/config ./internal/cmd` is still compiling/running.
