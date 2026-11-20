Exported `NamespaceEnv` and `ReleaseNameEnv` and used them for the Kubernetes backend’s environment reads. The tests now explicitly set both required variables, check the missing-variable errors, and verify the namespace and release configuration.

Verification passed: `go test -count=1 ./lib/backend/kubernetes` and `git diff --check`.