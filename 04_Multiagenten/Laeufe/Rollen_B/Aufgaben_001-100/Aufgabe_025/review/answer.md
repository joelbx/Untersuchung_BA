VERDICT: FIX

The patch resolves `${VAR}` values during `Unmarshal`, but [Load](/app/internal/config/config.go:199) reads configuration values earlier to select experimental fields and set defaults. For example, `storage.type: ${STORAGE_TYPE}` with `STORAGE_TYPE=local` misses the local path default; [validation](/app/internal/config/storage.go:116) can then dereference a nil `Local`. Resolve references before those Viper reads while preserving `FLIPT_` override precedence and the hook’s position in `DecodeHooks`.

Both relevant test commands passed:

- `GOPROXY=off GOSUMDB=off go test ./internal/config -run 'Test(EnvSubstitutionHook|LoadEnvReferences|Load)$' -count=1`
- `GOPROXY=off GOSUMDB=off go test -mod=readonly ./internal/config -count=1`

No TEST_ENVIRONMENT_PROBLEM. I made no project code changes.