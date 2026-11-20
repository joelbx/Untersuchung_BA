Implemented database dependency metadata for each authentication method: JWT is database free; token, OIDC, GitHub, and Kubernetes require the database. `authenticationGRPC` now uses an in-memory auth store when no enabled method needs persistent storage, while keeping JWT authentication active. Cleanup now runs only for enabled, database-backed methods.

Updated configuration and cleanup tests. Validation passed:

`GOMAXPROCS=2 go test -p 1 ./internal/config ./internal/cleanup ./internal/cmd`

[Authentication configuration](/app/internal/config/authentication.go) · [Auth startup](/app/internal/cmd/authn.go) · [Cleanup service](/app/internal/cleanup/cleanup.go)