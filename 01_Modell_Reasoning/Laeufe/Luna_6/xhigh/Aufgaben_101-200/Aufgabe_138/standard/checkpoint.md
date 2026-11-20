# Checkpoint

Issue: make OCI bundle manifest version configurable (1.0 or 1.1), defaulting to 1.1, with configuration validation and a public `WithManifestVersion` option.

Implemented the `storage.oci.manifest_version` default and validation, added the CUE and JSON schema field, and connected the configured value to OCI bundle packing through `WithManifestVersion`. Added configuration and bundle packing coverage for both versions.

Verification passed: `go test ./internal/config ./internal/oci ./config ./internal/storage/fs/store ./cmd/flipt` and `git diff --check`.
