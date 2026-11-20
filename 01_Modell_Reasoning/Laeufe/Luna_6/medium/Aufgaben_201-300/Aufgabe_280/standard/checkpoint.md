# Checkpoint

Implemented the Kubernetes backend environment variable fix:

- Exported `NamespaceEnv` and `ReleaseNameEnv` and used them for all corresponding backend reads.
- `NewWithClient` validates `KUBE_NAMESPACE` and `TELEPORT_REPLICA_NAME` and builds `Config.Namespace` and `Config.ReleaseName` from the named constants.
- Updated backend tests to set both required environment variables in every test case, including empty-value cases.

Verification: `go test ./lib/backend/kubernetes` passed; `git diff --check` passed.
