Implemented `x-flipt-accept-server-version` handling in the gRPC unary interceptor and registered it in the server chain. Handlers can retrieve the parsed version through `FliptAcceptServerVersionFromContext`; missing or invalid headers fall back to `v1.0.0`. Both `v1.0.0` and `1.0.0` formats are accepted.

Tests passed: `go test ./internal/server/middleware/grpc ./internal/cmd`.