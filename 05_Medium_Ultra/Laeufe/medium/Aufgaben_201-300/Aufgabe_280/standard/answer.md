Updated the Kubernetes backend to export and use `NamespaceEnv` (`KUBE_NAMESPACE`) and `ReleaseNameEnv` (`RELEASE_NAME`). Tests now explicitly set the namespace and replica variables and check the exact errors for missing values and the resulting configuration.

`go test ./lib/backend/kubernetes` and `git diff --check` passed.