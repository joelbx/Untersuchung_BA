Exported `NamespaceEnv` and `ReleaseNameEnv`, and updated the backend to use them when reading environment values. Added tests for missing-variable errors and environment-derived configuration; updated existing tests to set namespace and replica variables explicitly.

`go test ./lib/backend/kubernetes` passed.

- [kubernetes.go](/app/lib/backend/kubernetes/kubernetes.go)
- [kubernetes_test.go](/app/lib/backend/kubernetes/kubernetes_test.go)