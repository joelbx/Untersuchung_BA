# Checkpoint

Task: Fix teleport-kube-agent Kubernetes backend environment variable handling.

Completed:
- Exported `NamespaceEnv` and `ReleaseNameEnv` and used them to read namespace and release name in the Kubernetes backend.
- Kept constructor validation for both namespace and replica name, with the requested error format.
- Updated backend tests to explicitly set namespace and `TELEPORT_REPLICA_NAME`; added coverage for missing variables and environment-derived configuration.

Verification: `go test ./lib/backend/kubernetes` passed; `git diff --check` passed.
