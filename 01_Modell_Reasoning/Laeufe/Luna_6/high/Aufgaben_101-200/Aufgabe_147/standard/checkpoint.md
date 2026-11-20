# DeviceConfig overwrite issue checkpoint

- Objective: make DeviceConfig loading non-destructive, preserve/migrate the underscored persisted schema, and verify with existing repository tests.
- Repository: `/app`.
- Initial inspection: `rg` is unavailable in this environment; using `find`/`sed` instead.
- Changes and test results will be recorded here as work proceeds.

## Implementation and verification

- Refactored `DeviceConfig` persistence into one config object and explicit `Version`/`LocalStorageKey` static properties and constructor parameters.
- Loading now deserializes `_credentials` to a Map, only writes for migrations or token generation, preserves recognized underscored fields, and recovers from invalid/unavailable storage.
- v2 array credentials migrate to an object keyed by userId; the in-memory Map uses those IDs.
- `npm run types -- --pretty false`: passed.
- Client test command was attempted, but the harness failed before running tests because its `better-sqlite3` native build failed (`fatal error: opening dependency file ... No such file or directory`); npm also reported the installed `better-sqlite3` package as invalid. No test assertions ran.
- `git diff --check`: passed.
