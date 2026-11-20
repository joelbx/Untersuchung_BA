Implemented client version handling in [middleware.go](/app/internal/server/middleware/grpc/middleware.go): the interceptor reads the metadata header, accepts versions with or without `v`, and stores the parsed version in context. Missing or invalid values fall back to `0.0.0`.

Added coverage for both formats and fallback behavior in [middleware_test.go](/app/internal/server/middleware/grpc/middleware_test.go).

Validation passed: `go test ./internal/server/middleware/grpc` and `git diff --check`.