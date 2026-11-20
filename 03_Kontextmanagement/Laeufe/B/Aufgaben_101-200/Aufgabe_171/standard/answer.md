Implemented and registered the gRPC version header interceptor. It stores valid `v1.0.0` and `1.0.0` versions in the request context and falls back to `1.0.0` when the header is missing or invalid.

Tests passed: `go test ./internal/server/middleware/grpc ./internal/cmd`.