Implemented OCI configuration and storage wiring:

- Added OCI reference validation with the required unsupported-scheme error, plus parsing for `bundles_directory`, authentication, and `poll_interval`.
- Added `DefaultBundleDir()` and changed `NewStore` to accept its bundles root.
- Wired OCI storage into the gRPC server and bundle CLI, including credentials and polling.
- Updated both config schemas and registered `fs/oci` in the integration suite and CI matrix.

Verification passed: `go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./cmd/flipt ./build/testing`, `go test ./config`, and `git diff --check`. The Dagger-backed integration suite was compiled but not run.