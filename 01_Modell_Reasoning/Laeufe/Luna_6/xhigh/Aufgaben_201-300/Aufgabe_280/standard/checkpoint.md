# Checkpoint

Task: Resolve the teleport-kube-agent Kubernetes backend environment-variable issue.

Completed:
- Exported `NamespaceEnv` and `ReleaseNameEnv` and used them for all namespace and Helm release environment reads.
- Kept `NewWithClient()` validation for the namespace and replica name, with exact missing-variable error coverage.
- Added constructor config coverage and updated backend tests to explicitly set namespace and replica environment variables.
- Verified with `go test ./lib/backend/kubernetes` (passed).
