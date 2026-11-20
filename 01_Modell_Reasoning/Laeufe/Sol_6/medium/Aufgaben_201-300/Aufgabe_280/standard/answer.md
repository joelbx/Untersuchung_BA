Updated the Kubernetes backend to export and use `NamespaceEnv` and `ReleaseNameEnv`. `NewWithClient()` checks both required variables and returns the specified error when either is empty. The tests now set the simulated environment explicitly and cover constructor configuration and validation.

`go test ./lib/backend/kubernetes` and `git diff --check` passed.