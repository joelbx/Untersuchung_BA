Implemented the gRPC version header interceptor and context helpers. It accepts `v1.0.0` and `1.0.0`, and uses `1.0.0` when the header is missing or invalid.

Added tests for those cases. `go test ./internal/server/middleware/grpc` passes.