# OCI storage configuration fix

Status: implemented and verified in checked-out files.

Changes: OCI repository validation now uses the OCI reference parser; the config and JSON/CUE schemas accept OCI, bundle directory, authentication, and duration poll interval. Added DefaultBundleDir, passed explicit bundle root into NewStore, connected OCI config to the gRPC filesystem store, and registered fs/oci in build and CI integration matrices.

Verification: go test ./config ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./build/testing ./cmd/flipt passed. git diff --check passed. The Dagger integration matrix itself was not executed because it requires external images/services.
