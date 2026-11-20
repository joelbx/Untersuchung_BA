Exported `NamespaceEnv` and `ReleaseNameEnv` and updated the Kubernetes backend to use them. Tests now set the required environment variables explicitly and cover the exact missing-variable errors, configuration values, and release annotations.

`go test ./lib/backend/kubernetes` and `git diff --check` passed.