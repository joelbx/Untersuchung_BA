# Checkpoint

Task: validate required GitHub and OIDC authentication configuration at startup, including GitHub `read:org` scope.

Status: inspecting local config and tests. Assigned test-driven-development workflow in progress.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Implemented and verified: `go test ./internal/config -count=1` passed. Regression test first failed on missing GitHub/OIDC fields and provider-less scope error, then passed after implementation.

Full suite command: `GOPROXY=off go test ./...` is running. So far `internal/cache/redis` tests `TestSet`, `TestGet`, and `TestDelete` fail because Docker daemon is unavailable (`Cannot connect to the Docker daemon at unix:///var/run/docker.sock`).

Full suite completed with exit code 1. Additional failure: `internal/gitfs` `Test_FS_Submodule` attempted `https://github.com/flipt-io/flipt-gitops-test.git/info/refs?service=git-upload-pack` and received `Forbidden`; external research/network is blocked. Other packages, including `internal/config`, passed. Uncertainty: suite-wide green status cannot be established in this environment because Docker is unavailable and the submodule test requires external access.
