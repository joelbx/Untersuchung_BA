VERDICT: ACCEPT
Reviewed the applied diff across configuration schema/loading, OCI bundle building, CLI, and filesystem storage. The configuration defaults to 1.1, accepts 1.0, rejects 1.2 with the required error, and passes the selected ORAS version to PackManifest through WithManifestVersion. No correctness or regression issue found.

Tests: `go test ./internal/config ./internal/oci ./internal/storage/fs/store ./internal/storage/fs/oci ./cmd/flipt` exited 0. config, oci, and fs/oci passed; fs/store and cmd/flipt have no test files. `git diff --check` exited 0. No TEST_ENVIRONMENT_PROBLEM.
