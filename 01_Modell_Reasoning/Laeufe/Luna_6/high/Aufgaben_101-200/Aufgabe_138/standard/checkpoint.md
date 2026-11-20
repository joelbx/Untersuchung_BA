# Checkpoint

Implemented configurable OCI manifest versions.

- Added `storage.oci.manifest_version` to config and the JSON schema, with default `1.1` and accepted values `1.0` / `1.1`.
- Config loading now rejects unsupported values with the required validation error.
- Added `oci.WithManifestVersion` and wired configured values into both bundle CLI store creation and the filesystem OCI store.
- Bundle building uses the configured ORAS manifest version; direct store construction defaults to ORAS 1.1.
- Added config fixtures and tests for explicit 1.0, omitted/default 1.1, and invalid 1.2.

Verification: `go test ./internal/config ./internal/oci ./internal/storage/fs/store ./cmd/flipt` passed; `git diff --check` passed.
