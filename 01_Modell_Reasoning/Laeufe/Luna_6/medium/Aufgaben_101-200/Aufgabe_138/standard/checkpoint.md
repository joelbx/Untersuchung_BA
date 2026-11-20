# Checkpoint

Task: make OCI bundle manifest version configurable, default to 1.1, validate only 1.0/1.1, and use the configured value when building bundles.

Initial discovery: `rg` is unavailable in this environment; switching to basic filesystem tools. No repository files have been changed yet except this checkpoint.

Implementation complete: OCI config now defaults `manifest_version` to `1.1` and rejects unsupported values with the required error. `oci.WithManifestVersion` configures bundle packing; the runtime factory maps configured `1.0`/`1.1` to ORAS versions. Both schema formats and config fixtures/tests were updated.

Verification: `go test ./internal/config ./internal/oci ./internal/storage/fs/store` passed; `go test ./internal/config ./internal/oci` passed again after adding invalid-version coverage. `git diff --check` passed.
