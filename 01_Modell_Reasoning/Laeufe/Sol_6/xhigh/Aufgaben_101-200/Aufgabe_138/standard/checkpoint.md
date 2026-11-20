# OCI manifest version fix

Task: add configurable OCI manifest version 1.0 or 1.1, default 1.1, validate configuration, and apply it when building bundles.

Status: complete. Added schema and configuration support for OCI manifest versions 1.0 and 1.1, defaulting to 1.1 and rejecting unsupported values. Bundle creation uses the configured version through `WithManifestVersion`. Added configuration and bundle tests, including the inactive-storage OCI section case.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config ./internal/oci ./config ./cmd/flipt` passed; `git diff --check` passed.
