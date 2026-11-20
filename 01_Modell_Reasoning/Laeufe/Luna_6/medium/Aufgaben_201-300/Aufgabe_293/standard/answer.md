Implemented OCI configuration parsing and validation, added `DefaultBundleDir`, updated the store constructor and server wiring, and registered `fs/oci` in the build and CI matrices.

All relevant tests passed: `go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd` and `go test ./build/testing`.