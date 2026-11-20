Task: make OCI manifest version configurable (1.0 or 1.1), default 1.1, validate during config load, pass through bundle creation.
Status: complete. Added schema/config field and validation, WithManifestVersion option, wiring in storage backend and bundle command, config fixtures and build-manifest test.
Verification: go test ./internal/config ./internal/oci ./internal/storage/fs/store ./cmd/flipt ./config; go test ./internal/storage/fs/oci; git diff --check. All passed.
Constraints observed: no git history, index baseline, or harness configuration changes; local code/tests only.
