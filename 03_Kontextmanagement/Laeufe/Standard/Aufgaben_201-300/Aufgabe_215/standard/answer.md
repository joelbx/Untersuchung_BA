Added HTTPS support for the REST API, UI, and gRPC endpoint. Configuration now accepts a protocol, separate HTTP and HTTPS ports, and certificate paths; HTTPS startup validates the required files. HTTP remains the default.

Added configuration and handler tests. `go test ./...` and `git diff --check` pass.