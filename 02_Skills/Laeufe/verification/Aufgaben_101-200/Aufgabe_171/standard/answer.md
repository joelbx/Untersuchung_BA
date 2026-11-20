Implemented `x-flipt-accept-server-version` handling in the gRPC unary interceptor. It accepts versions with or without `v`, stores the parsed version in request context, and uses `1.0.0` when the header is missing or invalid. The interceptor is registered in the server chain.

Verification passed: `go test ./internal/server/middleware/grpc ./internal/cmd` and `git diff --check`.