# Checkpoint

Task: Fix teleport-kube-agent backend environment variable constants, constructor validation, and relevant tests.

Completed: Exported NamespaceEnv and ReleaseNameEnv, used them for namespace and release-name reads, and made backend tests set both required environment variables explicitly. Added constructor tests for missing variables, populated config, and Helm annotations.

Verification: GOPROXY=off go test ./lib/backend/kubernetes passed. git diff --check passed.

Delegation: None; solved directly.
