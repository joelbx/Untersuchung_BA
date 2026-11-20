Added `http` and `https` configuration, separate ports, and certificate and key validation. HTTPS now serves the REST API and UI over TLS, and the gRPC endpoint and REST gateway use TLS as well. Existing HTTP configurations retain their defaults.

Added a configuration test and updated the sample YAML. `go test ./cmd/flipt` and `git diff --check` pass.