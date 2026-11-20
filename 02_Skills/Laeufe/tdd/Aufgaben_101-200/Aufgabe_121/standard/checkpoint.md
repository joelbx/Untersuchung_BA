# Checkpoint

Task: add `flipt.is_auth_method` Rego built-in with readable authentication method names.

Implemented `internal/server/authz/engine/ext/extentions.go` and imported its registration from both authorization engine implementations. The built-in accepts an object and a string, maps token/oidc/kubernetes/k8s/github/jwt/cloud to the protocol enum values, returns a boolean for method matches, and returns the requested errors for missing authentication and unsupported labels.

TDD: `GOPROXY=off go test ./internal/server/authz/engine/ext -run TestIsAuthMethod -count=1` first failed as expected with `rego_type_error: undefined function flipt.is_auth_method`; after implementation it passed.

Checks:
- `GOPROXY=off go test ./internal/server/authz/...` passed.
- `git diff --check` passed.
- `GOPROXY=off go test ./...` failed in unrelated environment dependent tests:
  - `internal/cache/redis`: `TestSet`, `TestGet`, `TestDelete` failed with `create container: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`
  - `internal/gitfs`: `Test_FS_Submodule` failed with `Get "https://github.com/flipt-io/flipt-gitops-test.git/info/refs?service=git-upload-pack": Forbidden`.

No dependencies were downloaded. The complete suite remains unverified because these external services are unavailable; all authorization packages passed in both targeted and full runs.
