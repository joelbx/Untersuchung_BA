Implemented the OCI configuration and integration updates.

- Added OCI poll interval parsing and validation for unsupported repository schemes, with the required error message.
- Updated `NewStore` to take the bundles root directory and exposed `DefaultBundleDir()`.
- Registered `fs/oci` in the integration test matrix and CI workflow.
- Updated the existing `NewStore` call sites.

Verified with `go test ./internal/config ./internal/oci ./internal/storage/fs/oci`; all passed. The `fs/oci` suite is registered, but the Dagger integration suite was not run.