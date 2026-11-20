Implemented client version handling in [middleware.go](/app/internal/server/middleware/grpc/middleware.go:31): the interceptor reads and parses the metadata, accepts versions with or without a `v` prefix, and stores the version in context. Missing or invalid values fall back to `0.0.0`. The interceptor is wired into the server chain in [grpc.go](/app/internal/cmd/grpc.go:183).

Both existing test commands passed:

- `GOPROXY=off go test ./internal/server/middleware/grpc`
- `GOPROXY=off go test ./internal/cmd`

`git diff --check` passed.