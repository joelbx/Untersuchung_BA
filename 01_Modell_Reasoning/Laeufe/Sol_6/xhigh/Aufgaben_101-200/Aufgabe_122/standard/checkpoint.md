# Checkpoint

Task: implement storage.readOnly configuration and validation, expose it to the UI, show backend and read-only badges, and avoid a database connection during unauthenticated non-database bootstrap.

Status: implementation complete. `go test ./internal/config ./internal/cmd` passes with `GOPROXY=off`. UI test execution is unavailable because Node/npm are not installed in this workspace. Frontend selector cases are covered in `ui/src/app/meta/metaSlice.test.ts`.

Changed files: internal/config/{config.go,storage.go,config_test.go,testdata/storage/database_readonly.yml,testdata/storage/invalid_readonly.yml}, internal/cmd/{auth.go,auth_test.go}, ui/src/{types/Meta.ts,app/meta/metaSlice.ts,app/meta/metaSlice.test.ts,components/Header.tsx}.
