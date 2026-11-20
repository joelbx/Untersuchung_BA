Implemented configurable OCI manifest versions. `manifest_version` now accepts `"1.0"` or `"1.1"`, defaults to `"1.1"`, and returns the required validation error for unsupported values. The selected version reaches bundle creation through `WithManifestVersion` in both the CLI and storage paths.

Updated the config schemas and added coverage for config loading, invalid values, the default, and emitted bundle manifests. See [storage.go](/app/internal/config/storage.go:72), [file.go](/app/internal/oci/file.go:73), and [bundle.go](/app/cmd/flipt/bundle.go:161).

Verification passed: `go test ./config ./internal/config ./internal/oci ./internal/storage/fs/store ./cmd/flipt`.