# OCI storage configuration issue — complete

Implemented and reviewed:
- OCI repository required validation and the specified unsupported scheme error.
- OCI bundle directory, authentication, and duration based poll interval config fields.
- `config.DefaultBundleDir()` creates and returns Flipt's default OCI bundle directory.
- `oci.NewStore(logger, dir, ...)` uses the supplied bundle root; server and bundle CLI pass the configured/default root.
- OCI filesystem suite registered as `fs/oci` in the build/testing matrix and CI workflow.

Verification passed:
`go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./cmd/flipt ./build/testing`
`git diff --check`
