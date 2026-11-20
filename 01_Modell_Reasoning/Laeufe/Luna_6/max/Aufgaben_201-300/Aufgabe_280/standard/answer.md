Implemented the env variable fixes in [kubernetes.go](/app/lib/backend/kubernetes/kubernetes.go) and updated its tests in [kubernetes_test.go](/app/lib/backend/kubernetes/kubernetes_test.go).

`NamespaceEnv` and `ReleaseNameEnv` now drive the corresponding reads. Tests explicitly set the backend environment and verify missing-variable errors and loaded config values.

Verification passed: `GOPROXY=off GOTOOLCHAIN=local go test ./lib/backend/kubernetes`.