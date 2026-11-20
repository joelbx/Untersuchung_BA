# Checkpoint

Task: make OCI bundle manifest version configurable as 1.0 or 1.1, defaulting to 1.1, with configuration validation and tests.

Completed: added `storage.oci.manifest_version` to Go configuration and CUE/JSON schemas; set 1.1 as the default; reject unsupported versions with the required error; wired `WithManifestVersion` into server and CLI bundle store construction; used the selected ORAS version when building manifests.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/oci ./config ./internal/storage/fs/store ./cmd/flipt` passed. `git diff --check` passed.
