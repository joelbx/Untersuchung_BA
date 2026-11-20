Exported `NamespaceEnv` and `ReleaseNameEnv` and used them when the Kubernetes backend reads its namespace and release name. Updated the tests to set required variables explicitly and verify the missing-variable errors and constructor configuration.

`go test ./lib/backend/kubernetes` and `git diff --check` passed.