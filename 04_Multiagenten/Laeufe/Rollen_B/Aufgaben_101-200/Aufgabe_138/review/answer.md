VERDICT: ACCEPT

The applied patch defaults `storage.oci.manifest_version` to `"1.1"`, accepts `"1.0"`, rejects unsupported values with the required error, and uses `WithManifestVersion` when building bundles. I found no correctness issue.

`go test ./internal/config ./internal/oci ./internal/storage/fs/store ./internal/storage/fs/oci ./cmd/flipt` exited 0. The config, OCI, and OCI snapshot tests passed; the other two packages have no test files. `git diff --check` also exited 0. No TEST_ENVIRONMENT_PROBLEM.