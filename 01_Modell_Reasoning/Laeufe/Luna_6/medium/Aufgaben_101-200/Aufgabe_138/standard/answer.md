Implemented configurable OCI manifest versions. OCI storage defaults to `"1.1"`, validates only `"1.0"` and `"1.1"` with the required error, and passes the selected ORAS version into bundle creation via `WithManifestVersion`.

Updated both configuration schemas and added config coverage for loading `"1.0"` and rejecting `"1.2"`.

Verification passed: `go test ./internal/config ./internal/oci ./internal/storage/fs/store` and `git diff --check`.