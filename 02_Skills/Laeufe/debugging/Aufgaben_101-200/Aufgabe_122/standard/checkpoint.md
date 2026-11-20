# Checkpoint

Task: add validated storage.readOnly configuration and UI visibility; guard authentication bootstrap for non-database storage.

Status: investigating root causes and local tests.

Root cause: StorageConfig omits ReadOnly, so Viper discards the YAML key; metaSlice infers readonly from type; authenticationGRPC shortcut only names Git and Local, leaving Object to call getDB. Header badge uses a generic dot.

Pattern: existing optional config fields use pointers to preserve absence; config validation runs after Viper unmarshal; metadata JSON marshals Config directly. Existing UI components consume selectReadonly.

Hypothesis: adding a *bool ReadOnly field and rejecting non-database types when non-nil will enforce both true and false settings. A selector derived from config with a type-based fallback will keep UI state consistent. Changing the auth shortcut to all non-database types will avoid getDB for object storage.

Minimal reproduction: `GOPROXY=off go test ./internal/config -run 'TestLoad/read.only.setting.unsupported' -count=1` exits 1. YAML and ENV cases load without the expected error. Existing test harness panicked on nil error; added require.Error in YAML branch, and will add it in ENV branch.

Additional root-cause finding: `GOPROXY=off go test ./internal/config ./internal/cmd -count=1` failed after adding a database readOnly load test: `TestLoadDatabaseReadOnly` got nil. The experimental filesystem gate skips the whole StorageConfig when disabled, including database-only settings. The default database type is also lost by that skip. Adjusting the gate for database storage and expected default metadata.

Second edge case: a non-database readOnly setting without the filesystem experiment was silently skipped. `GOPROXY=off go test ./internal/config -run TestLoadReadOnlyUnsupportedWithoutExperiment -count=1` exited 1 with nil error. Bound environment keys before deciding whether to skip storage, and decode explicitly defined readOnly settings so validation rejects them.

UI check unavailable: `npm test -- --runInBand` from `/app/ui` exits 127 with `/bin/bash: line 1: npm: command not found`. UI behavior and TypeScript compile remain unverified by executable tooling.

Final verification: `GOPROXY=off go test ./internal/config ./internal/cmd -count=1` exits 0; both packages pass. `git diff --check` exits 0. Frontend execution remains unverified because npm and node are unavailable. No dependencies were downloaded.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`); using local find/grep.
