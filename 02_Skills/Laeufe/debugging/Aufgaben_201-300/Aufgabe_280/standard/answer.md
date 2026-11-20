Exported `NamespaceEnv` and `ReleaseNameEnv` and used them for the backend’s environment lookups. Updated the tests to set the required variables explicitly and verify both missing-variable errors and the resulting configuration.

The Kubernetes backend tests and `git diff --check` pass.