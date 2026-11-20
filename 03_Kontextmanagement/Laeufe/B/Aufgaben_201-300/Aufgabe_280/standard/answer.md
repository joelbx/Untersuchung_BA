Resolved the Kubernetes backend environment handling. It now exports `NamespaceEnv` and `ReleaseNameEnv`, uses them to configure the namespace and release name, and validates that the namespace and replica name are set. The tests explicitly set the required variables and cover missing values and configuration.

`go test ./lib/backend/kubernetes` and `git diff --check` passed.