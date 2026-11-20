# Checkpoint

Updated the Kubernetes backend to export and use `NamespaceEnv` and `ReleaseNameEnv`. Tests now explicitly set namespace and replica variables, and a constructor test checks missing-variable errors and the resulting config. `go test ./lib/backend/kubernetes` passed; `git diff --check` passed.
