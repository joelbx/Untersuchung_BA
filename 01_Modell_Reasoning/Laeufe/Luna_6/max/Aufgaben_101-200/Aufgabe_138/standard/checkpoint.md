# Checkpoint

Task: make OCI manifest version configurable, defaulting to 1.1, validate supported values 1.0/1.1, and propagate the selected version to OCI bundle creation through `WithManifestVersion`.

Implementation in progress:

- Added OCI `manifest_version` to configuration decoding, with the 1.1 default and exact validation error for unsupported values.
- Added the 1.0/1.1 choices to both CUE and JSON schemas.
- Added `WithManifestVersion`, defaulted new OCI stores to 1.1, and wired configured values into both backend storage and CLI bundle store construction.
- Added config loading fixtures/cases and a bundle test that inspects the emitted manifest version.

Verification complete:

- `gofmt` applied to edited Go files; `git diff --check` is clean.
- `go test ./config ./internal/config ./internal/oci ./internal/storage/fs/store ./cmd/flipt` passes.
- The config tests cover explicit 1.0, default 1.1, and rejection of 1.2. The OCI build test inspects the emitted manifest for both the default and configured 1.0 versions.
