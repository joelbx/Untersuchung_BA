Implemented the Kubernetes backend environment variable fix.

- Exported and used `NamespaceEnv` and `ReleaseNameEnv`.
- Kept `NewWithClient()` validation for the namespace and replica name, with the requested error message.
- Updated tests to set both required environment variables explicitly and cover missing variables plus configuration loading.

`go test ./lib/backend/kubernetes` and `git diff --check` passed.