Implemented configurable OCI manifest versions. The OCI config now defaults to `1.1`, accepts `1.0` or `1.1`, and returns the requested validation error for unsupported values. Bundle creation uses the configured version through `WithManifestVersion`.

Updated both config schemas and added coverage for config loading, invalid values, and bundle manifest options.

Verified: `go test ./internal/config ./internal/oci ./internal/storage/fs/store` and `git diff --check` passed.