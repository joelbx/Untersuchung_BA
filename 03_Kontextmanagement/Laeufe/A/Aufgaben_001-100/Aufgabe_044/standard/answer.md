Fixed namespace listing for users without access to `default`. Both authorization engines now evaluate viewable namespaces, middleware passes the result through request context, and `ListNamespaces` filters before pagination and reports the visible count.

Verified with `go test ./internal/server/authz/... ./internal/server -count=1` and `git diff --check`.