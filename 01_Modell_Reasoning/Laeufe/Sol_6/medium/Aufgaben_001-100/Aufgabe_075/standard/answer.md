Added a `user_props` table and a context-scoped `UserPropsRepository`, exposed through `DataStore.UserProps`. The migration transfers existing Last.fm session keys, and Last.fm now stores them under the `sessionKeyProperty` constant. Property error logs include a request ID where available.

Verified with `go test ./...` and `git diff --check`; both passed.