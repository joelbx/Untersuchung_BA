Implemented user-scoped properties in `/app`. A new migration creates `user_props` and moves existing Last.fm session keys; `DataStore.UserProps` now exposes a context-scoped repository. Last.fm uses the `sessionKeyProperty` constant, and property error logs include request IDs where available.

Repository and migration tests were added. `go test ./...` passes.