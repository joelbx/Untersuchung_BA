# Checkpoint

Task: Fix OCI storage configuration parsing and validation, ensure OCI store uses its bundle directory, and register `fs/oci` in build/test and CI integration matrices.

Completed:
- Added OCI config duration and made authentication YAML/JSON fields decodable.
- Added scheme-aware OCI repository validation and `config.DefaultBundleDir()`.
- Updated OCI store constructor to accept its bundle root and wired OCI source into server startup.
- Registered `fs/oci` in the build/testing matrix and CI workflow.

Verification: `go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd` and `go test ./build/testing` passed.
