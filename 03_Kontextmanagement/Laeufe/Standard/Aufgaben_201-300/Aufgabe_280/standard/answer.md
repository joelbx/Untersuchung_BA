Exported `NamespaceEnv` and `ReleaseNameEnv` and used them for the backend’s namespace and release name reads. The tests now set the required variables explicitly, verify the missing-variable errors, and check constructor configuration.

`go test ./lib/backend/kubernetes` passed using local dependencies.