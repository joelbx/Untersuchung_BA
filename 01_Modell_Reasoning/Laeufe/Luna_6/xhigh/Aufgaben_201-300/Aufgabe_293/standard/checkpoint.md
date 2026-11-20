# Checkpoint

Task: resolve OCI storage configuration parsing and validation gaps in `/app`.

Implemented:
- OCI config now validates references through the OCI parser, returns the required scheme error, safely handles a missing OCI block, and parses bundle directory, authentication, and poll interval settings.
- Added `DefaultBundleDir()` in `internal/config/storage.go`, including directory creation.
- Changed `internal/oci.NewStore` to accept and use an explicit bundles root, wired OCI configuration into gRPC storage and bundle CLI, including credentials and polling.
- Updated CUE/JSON schemas and registered `fs/oci` in the integration suite and CI matrix.

Verification:
- `go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./cmd/flipt ./build/testing` passed.
- `go test ./config` passed.
- `git diff --check` passed.
