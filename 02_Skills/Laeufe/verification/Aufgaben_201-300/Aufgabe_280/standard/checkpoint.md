# Checkpoint

Task: Fix Kubernetes backend environment variable handling and tests.

Changes:
- Exported `NamespaceEnv` and `ReleaseNameEnv` and used them for backend environment reads.
- Kept constructor validation for both required variables and made tests assert its exact errors.
- Made backend tests set namespace and replica variables explicitly, including empty values.
- Added a constructor test for namespace, replica, release name, secret name, and Helm annotations.

Verification:
- `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test -count=1 ./lib/backend/kubernetes`: passed (`ok ... 0.019s`, exit 0).
- `git diff --check`: passed (exit 0).
