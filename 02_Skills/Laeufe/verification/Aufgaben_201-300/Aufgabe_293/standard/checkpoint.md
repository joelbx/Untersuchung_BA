# OCI configuration work

Implemented OCI configuration validation through the OCI reference parser, schema fields for bundles directory and poll interval, default bundle directory creation, store directory and credentials wiring, and the `fs/oci` integration case and CI matrix entry. Added local bundle seed command for that integration case.

Verification:

- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test -count=1 ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/cmd ./build/testing ./build/internal/cmd/oci` — exit 0; four tested packages passed, two build packages have no test files.
- `bundle_test_dir=$(mktemp -d); GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go run ./build/internal/cmd/oci/... -testdata-dir build/testing/integration/readonly/testdata -bundle-dir "$bundle_test_dir" && test -f "$bundle_test_dir/testdata/index.json"` — exit 0, OCI index created.
- `git diff --check` — exit 0.

The Dagger `fs/oci` integration suite was not executed because it requires external container images; local execution would download dependencies. Its registration and helper package compiled in the focused Go test command. End-to-end container behavior remains unverified.
