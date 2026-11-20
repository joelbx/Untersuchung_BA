# Checkpoint

Task: make OCI bundle manifest version configurable (1.0 or 1.1), defaulting to 1.1, with configuration validation and tests.

Initial evidence: `internal/oci/file.go` hardcodes `oras.PackManifestVersion1_1_RC4`. `rg` is unavailable (`/bin/bash: rg: command not found`), so searches use `grep` and `find`.

Implementation: added `storage.oci.manifest_version` to the CUE and JSON schemas and configuration struct; default is `1.1`; configuration loading rejects unsupported values with the requested error. The OCI store now accepts `WithManifestVersion` and passes the selected ORAS version to `PackManifest`; the storage constructor selects 1.0 when configured. Added configuration fixtures and bundle manifest tests.

Verification: first `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/oci ./internal/storage/fs/store ./config` failed because the new test expected an empty 1.1 config media type; ORAS actually uses `application/vnd.oci.empty.v1+json`. Corrected the assertion. Fresh `GOPROXY=off GOSUMDB=off go test -count=1 ./internal/config ./internal/oci ./internal/storage/fs/oci ./internal/storage/fs/store ./config` passed (all tested packages; store has no test files). `git diff --check` passed.
