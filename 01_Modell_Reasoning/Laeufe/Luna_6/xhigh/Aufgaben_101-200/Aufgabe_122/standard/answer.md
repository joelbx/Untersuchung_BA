Implemented `storage.readOnly` with validation, including database configuration when experimental filesystem storage is disabled. Updated authentication bootstrap to skip database setup for non-database backends when authentication is disabled.

The UI now exports `selectConfig`, derives read-only mode from `config.storage.readOnly` with the required storage-type fallback, and shows the active backend icon in the header, including in the “Read-Only” badge.

Added the requested [invalid_readonly.yml](/app/internal/config/testdata/storage/invalid_readonly.yml) fixture and a database read-only config case.

**Validation:** `go test ./internal/config ./internal/cmd` and `git diff --check` passed. UI tests/build could not be run because the local UI toolchain is unavailable.