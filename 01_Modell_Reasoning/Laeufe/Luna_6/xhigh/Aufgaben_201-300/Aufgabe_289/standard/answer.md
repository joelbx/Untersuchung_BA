Implemented the config exports in [config.go](/app/internal/config/config.go): `DefaultConfig()` returns the standard defaults, `DecodeHooks` exposes the decode hooks, and `Load` composes hooks from that exported slice. Added the `version` mapstructure tag.

Changed `StorageConfig.Local` and `.Git` to pointers and made validation handle nil values in [storage.go](/app/internal/config/storage.go). Updated the existing storage test fixtures accordingly.

**Verification:** `go test ./internal/config ./internal/cmd` and `git diff --check` pass. This checkout does not contain `schema_test.go`, so I could not run that specific CUE validation test.