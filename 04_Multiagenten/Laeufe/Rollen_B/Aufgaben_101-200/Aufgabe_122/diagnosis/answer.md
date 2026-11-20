I traced the issue but did not change project source or tests. This session’s fault-localization instruction limits me to diagnosis, so the requested fix and `invalid_readonly.yml` remain unimplemented.

- [storage.go](/app/internal/config/storage.go:27) has no `ReadOnly` field, and `StorageConfig.validate()` does not reject a defined flag on non-database storage. The field needs to distinguish an absent value from explicit `false`.
- [Meta.ts](/app/ui/src/types/Meta.ts:12) lacks `IStorage.readOnly` and the `OBJECT` storage type. [metaSlice.ts](/app/ui/src/app/meta/metaSlice.ts:40) derives read-only solely from storage type and has no `selectConfig` export.
- [Header.tsx](/app/ui/src/components/Header.tsx:35) already shows a “Read-Only” badge, but its dot does not identify the backend.
- [auth.go](/app/internal/cmd/auth.go:47) skips the database connection for disabled authentication with git or local storage, but still attempts one for object storage.

The existing YAML and environment config cases in [config_test.go](/app/internal/config/config_test.go:613) provide the pattern for covering the required validation error. I recorded the findings in `.codex-role-output/checkpoint.md`; no tests were run.