# OCI storage configuration checkpoint

Task: fix OCI repository validation, configuration fields, bundle directory handling, and integration matrix registration.

Implemented: OCI reference validation via the OCI parser; missing repository handling; poll interval parsing/default; explicit bundle directory in NewStore; DefaultBundleDir under Flipt data directory; OCI gRPC startup wiring; CLI bundle directory wiring; fs/oci integration suite and CI matrix entry. Existing OCI config fixture now checks a 5m interval and unsupported scheme.

Verification: `go test ./internal/config ./internal/oci ./internal/storage/fs/oci` passed. `go test ./internal/cmd ./cmd/flipt ./build/testing` passed. `git diff --check` passed. Dagger integration suite was registered and compiled but not executed locally.
