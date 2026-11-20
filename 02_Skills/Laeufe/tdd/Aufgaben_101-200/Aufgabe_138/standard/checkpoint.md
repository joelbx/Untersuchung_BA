# Checkpoint

Task: configurable OCI manifest version, default 1.1, validation, and bundle construction.

Status: implementation complete. Configuration and OCI bundle tests pass.

TDD red: `go test ./internal/config -run '^TestLoadOCIManifestVersion$' -count=1` failed for the missing field/default and missing invalid-value error. `go test ./internal/oci -run '^TestStoreBuildManifestVersion$' -count=1` failed to compile because the requested `WithManifestVersion` interface was missing.

Verification: `go test ./internal/config ./internal/oci ./config ./internal/storage/fs/store` passed; `git diff --check` passed. `go test ./...` ran and failed in unrelated tests: `internal/cache/redis` (`TestSet`, `TestGet`, `TestDelete`) cannot connect to Docker daemon at `/var/run/docker.sock`; `internal/gitfs` (`Test_FS_Submodule`) attempted `https://github.com/flipt-io/flipt-gitops-test.git/info/refs?service=git-upload-pack` and received `Forbidden`. All other packages in that run passed or had no tests.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used grep/find.
