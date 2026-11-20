# Checkpoint

Task: add explicit `storage.readOnly` support across backend configuration, frontend state/header, and authentication bootstrap behavior.

Implemented:
- Added optional pointer `StorageConfig.ReadOnly` so omitted and explicit `false` remain distinct; non-database use is rejected with the requested validation message.
- Added the requested invalid object storage fixture and a config-load case that checks it.
- Changed authentication bootstrap to use in-memory auth storage for non-database backends when auth is disabled, while preserving the empty-type database default.
- Added `IStorage.readOnly?`, the `OBJECT` storage type, exported `selectConfig`, and derived `selectReadonly` from config with database as the missing-type default.
- Added a visible active-backend icon/name and a lock icon on the header's Read-Only badge.

Verification:
- `go test ./internal/config ./internal/cmd` passed.
- `git diff --check` passed.
- UI tests could not start: `npm test -- --runInBand` returned `npm: command not found`; no Node or TypeScript tooling is installed.
