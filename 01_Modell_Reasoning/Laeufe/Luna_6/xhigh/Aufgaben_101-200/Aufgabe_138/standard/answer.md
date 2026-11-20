Implemented configurable OCI manifest versions. The `storage.oci.manifest_version` field accepts `"1.0"` or `"1.1"`, defaults to `"1.1"`, and returns the required error for unsupported values. Bundle creation now applies the configured version through `WithManifestVersion`; the CLI and OCI storage setup both pass it through.

Updated the CUE and JSON schemas and added config and bundle tests for default, 1.0, and 1.1 behavior.

Verification passed: `go test ./internal/config ./internal/oci ./config ./internal/storage/fs/store ./cmd/flipt` and `git diff --check`.