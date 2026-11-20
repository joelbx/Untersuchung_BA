Implemented OCI storage configuration and runtime support.

- Added clear repository validation, including the required unsupported-scheme error, and parsed `bundles_directory`, `poll_interval`, and registry credentials.
- Added `config.DefaultBundleDir()` and changed OCI store construction to accept an explicit bundles root.
- Wired OCI storage into gRPC startup and registered `fs/oci` in the integration suite and CI matrix.
- Updated the CUE and JSON schemas and added config regression coverage.

Focused Go tests passed: `go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./config ./build/testing ./cmd/flipt ./internal/cmd`. I also verified the CLI builds a local OCI bundle from the integration fixtures. The full Dagger integration suite was not run.