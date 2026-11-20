# Checkpoint

Task: Make OCI bundle manifest version configurable, default to 1.1, and validate supported versions during configuration loading.

Initial status: Repository working tree was clean. `rg` is unavailable in this environment; using standard filesystem tools for discovery.

Implementation complete:
- Added OCI `manifest_version` config, default `1.1`, and exact validation for `1.0`/`1.1`.
- Added schema enum/default in CUE and JSON schemas.
- Added `oci.WithManifestVersion` and passed the selected ORAS version from OCI storage setup into `PackManifest`.
- Added config loading/invalid-value coverage and bundle manifest option coverage.

Verification: `go test ./internal/config ./internal/oci ./internal/storage/fs/store` passed; `git diff --check` passed.
