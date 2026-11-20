Task: Make OCI manifest version configurable as 1.0 or 1.1, default 1.1, validate configuration, and use it when building bundles.
Status: Complete. Added config field/default/validation, CUE and JSON schema entries, WithManifestVersion store option, server and bundle command wiring, config fixtures, and manifest output test.
Tests: go test ./internal/config ./internal/oci ./internal/storage/fs/store ./config ./cmd/flipt passed. git diff --check passed.
Constraints: Local repository and existing tests only. No git history, index baseline, or harness changes.
