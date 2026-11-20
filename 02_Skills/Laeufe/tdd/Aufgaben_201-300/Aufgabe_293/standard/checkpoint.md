# Checkpoint

Task: OCI storage configuration and integration matrix fixes.
Status: implementation and focused tests complete. Added a regression test for unsupported schemes without a repository path and reran the focused suites successfully.

Changes: OCI repository scheme validation, schema fields, poll interval decoding, default bundle directory, explicit NewStore directory, server OCI source wiring, and fs/oci integration registration/workflow case.

Checks:
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./build/testing ./cmd/flipt -count=1` passed.
- `git diff --check` passed.
- Local `/tmp/flipt-oci-check bundle build readonly:latest` against copied readonly fixtures and an explicit bundle directory produced a digest and OCI layout files.
- Rebuilt `/tmp/flipt-oci-check`, then launched it against the generated OCI bundle with `timeout 3 env XDG_CONFIG_HOME=... FLIPT_STORAGE_TYPE=oci FLIPT_STORAGE_OCI_REPOSITORY=flipt://local/readonly:latest FLIPT_STORAGE_OCI_BUNDLES_DIRECTORY=... /tmp/flipt-oci-check`; it remained running until timeout (exit 124), then printed `Error: context canceled`. Startup did not report an OCI error; request handling was not checked.
- `GOTOOLCHAIN=local GOPROXY=off go test ./...` failed in `internal/cache/redis` (`TestSet`, `TestGet`, `TestDelete`): `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?: failed to create container`. Other packages reported passing. Redis behavior remains unverified here.
- `GOTOOLCHAIN=local GOPROXY=off go test ./build/...` failed in `build/testing/integration/api` (`TestAPI`) and `build/testing/integration/readonly` (`TestReadOnly`): `dial tcp [::1]:9000: connect: connection refused`. These suites require a running Flipt service, so the new fs/oci Dagger case remains unexecuted here.
