# Checkpoint

Implemented configurable OCI manifest version under `storage.oci.manifest_version`. Configuration defaults to `1.1`, accepts `1.0` and `1.1`, and rejects all other values with `wrong manifest version, it should be 1.0 or 1.1`. Added schema entries, passed the selected ORAS version to OCI stores created by both server and bundle CLI paths, and added a public `WithManifestVersion` option. Bundle creation now uses the store option.

Added configuration fixtures/tests for default, explicit `1.0`, and invalid `1.2`, plus a bundle manifest test covering default `1.1` and explicit `1.0`.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config ./internal/oci ./internal/storage/fs/store ./config ./cmd/flipt` passed. `git diff --check` passed.
