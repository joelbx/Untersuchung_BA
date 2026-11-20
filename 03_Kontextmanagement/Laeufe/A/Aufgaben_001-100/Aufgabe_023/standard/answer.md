Fixed authentication startup so JWT with Local, Git, or OCI storage uses an in-memory auth store without connecting to a database. Each authentication method now declares `RequiresDatabase`, and cleanup runs only for enabled methods that require a database.

The updated configuration, cleanup, and startup tests pass: `go test ./internal/config ./internal/cleanup ./internal/cmd`.