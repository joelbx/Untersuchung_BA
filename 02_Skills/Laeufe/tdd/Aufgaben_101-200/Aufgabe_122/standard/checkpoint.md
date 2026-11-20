# Checkpoint

Task: add validated storage.readOnly configuration, frontend readonly behavior and header visibility, authentication bootstrap guard.

Status: inspecting repository. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

TDD tests added before implementation: config rejects explicit false on object, database readOnly metadata, authentication bootstrap for all non-database types, UI selector/default behavior.
UI test command `npm test -- --runInBand src/app/meta/metaSlice.test.ts` in /app/ui failed before executing: `/bin/bash: npm: command not found`. UI behavior remains unverified by Jest here; no dependencies downloaded.

Backend RED observations:
- `go test ./internal/config -run '^TestDatabaseStorageReadOnlyMetadata$' -count=1` failed: metadata lacked `readOnly`.
- `go test ./internal/config -run 'TestLoad/read_only_setting_on_object_storage|TestDatabaseStorageReadOnlyMetadata' -count=1` failed because invalid object readOnly was accepted (existing TestLoad error branch then panicked on nil error).
- `go test ./internal/cmd -run TestAuthenticationGRPCWithoutDatabaseStorage -count=1` failed for object storage with `opening db: error parsing url: <nil>, invalid database scheme`.

Backend GREEN: `go test ./internal/config ./internal/cmd -count=1` passed. `go test ./config -count=1` passed after adding `readOnly` to CUE schema.

Full suite: `go test ./...` failed. `config/Test_CUE` initially failed because CUE did not allow `storage.readOnly`; fixed and reran `go test ./config -count=1` successfully. `internal/cache/redis` tests `TestSet`, `TestGet`, `TestDelete` failed because Docker daemon is unavailable (`Cannot connect to the Docker daemon at unix:///var/run/docker.sock`). All other packages reported pass or no tests in the completed run. Full suite was not rerun after the CUE fix; affected packages are being rerun separately.

UI: Node/npm/Jest/tsc binaries are unavailable. Attempted UI tests were removed because this repository's Jest config lacks alias mapping and JSX transformation required by the new tests. UI behavior is source-reviewed only; not claimed as executed.
