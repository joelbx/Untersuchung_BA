HTTPS support is implemented for the REST API, UI, and gRPC endpoint. Configuration now accepts `server.protocol`, separate HTTP and HTTPS ports, and TLS certificate paths; startup checks HTTPS credentials while existing HTTP configurations keep their defaults.

I updated the configuration docs and added focused tests. `go test ./...` and `git diff --check` pass.