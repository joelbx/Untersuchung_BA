Updated the Kubernetes backend to use exported `NamespaceEnv` and `ReleaseNameEnv` constants. `NewWithClient()` now reads the namespace and release name through those constants, while its required-variable checks return the specified error. The tests now set the environment variables explicitly and verify the constructor errors and configuration.

`go test ./lib/backend/kubernetes` passed.