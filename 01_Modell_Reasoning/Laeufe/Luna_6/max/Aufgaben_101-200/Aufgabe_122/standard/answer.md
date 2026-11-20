Implemented `storage.readOnly` as an optional backend config field, with the requested validation error for non-database storage. Added the invalid object-storage fixture and config test. Authentication bootstrap now skips database setup for non-database storage when authentication is disabled, while treating an unset storage type as the database default.

The UI now exports `selectConfig`, derives read-only state from `config.storage.readOnly` with a storage-type fallback, and shows the active backend icon and a “Read-Only” badge when applicable.

**Verification:** `go test ./internal/config ./internal/cmd` passed, and `git diff --check` passed. UI tests could not run because npm and Node are unavailable.

Changed: [storage.go](/app/internal/config/storage.go), [auth.go](/app/internal/cmd/auth.go), [metaSlice.ts](/app/ui/src/app/meta/metaSlice.ts), [Header.tsx](/app/ui/src/components/Header.tsx), [Meta.ts](/app/ui/src/types/Meta.ts), and [invalid_readonly.yml](/app/internal/config/testdata/storage/invalid_readonly.yml).