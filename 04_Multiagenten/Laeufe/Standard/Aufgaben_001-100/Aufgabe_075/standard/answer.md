Added a `user_props` table and a context-scoped `UserPropsRepository`. The migration transfers existing Last.fm session keys, and Last.fm now uses the `sessionKeyProperty` constant instead of constructing user-prefixed keys. Property error logs include the request ID when available.

Added a test for user isolation, updates, and deletion. `go test ./...` and `git diff --check` pass.