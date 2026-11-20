Implemented the gRPC version interceptor and context helpers in [middleware.go](/app/internal/server/middleware/grpc/middleware.go), and added it to the server chain in [grpc.go](/app/internal/cmd/grpc.go). It accepts `v1.0.0` and `1.0.0` formats and uses `1.0.0` when the header is missing or invalid.

The relevant middleware and server package tests pass.