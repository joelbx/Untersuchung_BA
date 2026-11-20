Added a `user_props` table and a context-scoped `UserPropsRepository`. The migration moves existing Last.fm session keys into the new table, and Last.fm now uses the `sessionKeyProperty` constant without constructing user-prefixed keys. Property error logs include the request ID when available.

Verification: `GOPROXY=off go test ./...` and `git diff --check` both passed.