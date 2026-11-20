Implemented configurable OCI manifest versions. `manifest_version` now defaults to `1.1`, accepts `1.0` or `1.1`, and returns the required validation error for unsupported values. Bundle creation uses `WithManifestVersion` with the configured version.

Added config coverage for explicit `1.0`, the `1.1` default, and invalid `1.2`.

Verification passed: `go test ./internal/config ./internal/oci ./internal/storage/fs/store ./cmd/flipt` and `git diff --check`.