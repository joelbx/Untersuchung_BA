Implemented OCI storage configuration and runtime support, including repository validation, bundle directory handling, authentication parsing, and poll interval parsing. Added `config.DefaultBundleDir()`, updated `oci.NewStore` to accept its bundles root, and registered the `fs/oci` integration suite in the build and CI matrices.

Verification passed:

- `go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./cmd/flipt ./build/testing`
- `git diff --check`