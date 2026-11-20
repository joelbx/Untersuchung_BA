Implemented and registered the gRPC version interceptor. It reads `x-flipt-accept-server-version`, accepts `v1.0.0` and `1.0.0` formats, and makes the parsed version available through the new context helpers. Missing or invalid headers fall back to `1.0.0`.

`go test ./internal/server/middleware/grpc ./internal/cmd` passed.