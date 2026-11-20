# OCI storage configuration fix checkpoint

- Confirmed OCI configuration fields are partially present, but polling is absent, OCI config validation does not recognize URL schemes, and OCI is not selected by the gRPC storage factory.
- Confirmed OCI store currently chooses its own default root; the requested constructor takes an explicit root, and the config package needs the public `DefaultBundleDir` helper.
- Wired OCI validation, schema, runtime store/source construction, auth credentials, default bundle path, and the `fs/oci` CI integration entry.
- Focused tests pass: `go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./config ./build/testing ./cmd/flipt ./internal/cmd`.
- Verified local OCI bundle seeding with the CLI from `build/testing/integration/readonly/testdata`; it produced the bundle in the explicitly configured bundles directory.
