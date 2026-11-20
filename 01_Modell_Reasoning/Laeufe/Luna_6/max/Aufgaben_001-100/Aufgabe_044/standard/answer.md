Implemented namespace authorization across both engines, middleware, and the listing endpoint. Authorized namespace results are stored in context, filtered before pagination, and used to calculate `TotalCount`. Empty access lists are supported, and `*` grants access to all namespaces.

The authorization fixture and focused tests cover users with no roles, `devs`, `ops`, and both roles. The UI already selects the first namespace returned when its saved `default` is unavailable.

Tests passed:

- `go test ./internal/server/authz/... ./internal/server`
- `go test ./internal/cmd`
- `git diff --check`

Key changes: [authz.go](/app/internal/server/authz/authz.go), [middleware.go](/app/internal/server/authz/middleware/grpc/middleware.go), and [namespace.go](/app/internal/server/namespace.go).