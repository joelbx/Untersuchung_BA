Implemented user-scoped properties with a new `user_props` table and `UserPropsRepository`, exposed through `DataStore.UserProps`. The migration transfers existing Last.fm session keys and removes their legacy global-property entries.

Last.fm now uses the `sessionKeyProperty` constant and scopes OAuth callback writes through the user in context. Error logs include request IDs where available.

Verification: `go test ./...` passed; after the final SQL quoting change, `go test ./persistence ./core/agents/lastfm` and `git diff --check` passed.