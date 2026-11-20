# Fault localization progress

Inspected OCI config, loader, store, server wiring, schemas, and integration matrix. No project source or tests changed.

Findings:
- `internal/config/storage.go`: OCI validation uses `registry.ParseReference` instead of `oci.ParseReference`, so unsupported schemes do not produce the required error; `c.OCI` is dereferenced without nil guard. OCI struct omits `PollInterval`; default key is misspelled `store.oci.insecure`.
- `config/flipt.schema.cue` omits OCI bundles_directory and poll_interval; generated `config/flipt.schema.json` also omits them and omits `oci` from storage.type enum. OCI authentication already exists in both schemas and Go struct.
- `internal/oci/file.go`: `NewStore` gets root from private `defaultBundleDirectory`, not required explicit `dir`; private helper uses `config.Dir()` (user config path). `cmd/flipt/bundle.go` passes directory via option. Required `config.DefaultBundleDir()` absent.
- `internal/cmd/grpc.go`: storage switch has no OCI case, so server cannot start with storage.type oci. OCI source exists with poll interval option.
- `build/testing/integration.go` and `.github/workflows/integration-test.yml` lack fs/oci registration.
- Existing config tests cover OCI fields except poll_interval and unsupported-scheme exact error; existing invalid-reference fixture tests a bare registry.

Uncertainty: did not run tests (diagnosis-only specialist role and no downloads). The expected directory base should be checked against Flipt's data-directory convention when implementing `DefaultBundleDir`.
