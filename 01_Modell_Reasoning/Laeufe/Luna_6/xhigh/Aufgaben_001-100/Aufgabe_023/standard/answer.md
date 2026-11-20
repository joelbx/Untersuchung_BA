Implemented database dependency metadata for each authentication method. JWT is marked database independent; static token, OIDC, GitHub, and Kubernetes require a database.

Authentication startup now selects in-memory auth storage and oplocks when no enabled method requires a database, while still configuring JWT middleware. Cleanup startup and per-method cleanup both honor the database requirement.

Verified with `go test ./internal/config ./internal/cmd ./internal/cleanup` and a follow-up `go test ./internal/config`; all passed.