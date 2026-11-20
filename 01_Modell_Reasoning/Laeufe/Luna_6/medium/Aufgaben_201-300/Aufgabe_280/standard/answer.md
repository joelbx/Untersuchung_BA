Implemented the Kubernetes backend environment variable fix. `NamespaceEnv` and `ReleaseNameEnv` are exported and used for the corresponding reads, and the tests now set both required variables explicitly in every case.

Verification passed: `go test ./lib/backend/kubernetes` and `git diff --check`.