Implemented the Kubernetes backend environment variable updates in [kubernetes.go](/app/lib/backend/kubernetes/kubernetes.go): exported `NamespaceEnv` and `ReleaseNameEnv`, and used them for validation and configuration.

Updated the backend tests to set namespace and replica environment variables explicitly. `go test ./lib/backend/kubernetes` passes.