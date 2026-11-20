Implemented context-scoped user properties with a dedicated `user_props` table, composite user/key primary key, and migration of existing Last.fm session keys. Last.fm now reads and writes `LastFMSessionKey` through `UserPropsRepository`; callback persistence resolves the user from its ID and includes request IDs in error logs.

Added `model.UserPropsRepository` and `DataStore.UserProps`, with the SQL implementation in [user_props_repository.go](/app/persistence/user_props_repository.go) and schema migration in [20210622120000_create_user_props.go](/app/db/migration/20210622120000_create_user_props.go).

Verification passed: `go test ./persistence ./core/agents/lastfm`, `go test ./...`, and `git diff --check`.