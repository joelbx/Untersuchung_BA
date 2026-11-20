Added a `user_props` table and a context-scoped `UserPropsRepository`. The migration moves existing Last.fm session keys into the new table, and Last.fm now uses the `sessionKeyProperty` constant. Property error logs include the request ID when available.

Repository, migration, and Last.fm tests pass; `go test ./...` and `git diff --check` also pass.