# Checkpoint

Task: fix teleport-kube-agent backend environment handling and tests.

Completed:
- Exported NamespaceEnv and ReleaseNameEnv and used them for backend environment reads.
- Kept NewWithClient validation for required namespace and replica name, with namespace checked first.
- Made backend tests explicitly set namespace, replica name, and release name; added constructor error and configuration coverage.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./lib/backend/kubernetes` passed.
- `git diff --check` passed.
