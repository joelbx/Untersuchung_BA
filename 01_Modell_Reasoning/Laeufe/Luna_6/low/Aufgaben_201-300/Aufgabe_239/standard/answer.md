Updated `UserPropsRepository` and `MockedUserPropsRepo` so every operation takes an explicit user ID. Persistence scopes queries by that ID, and the mock uses a stable composite key.

LastFM session reads and writes now use the provided user ID. Link status and unlink use the authenticated user; the callback resolves the requested account before saving its session key.

Relevant tests passed: `go test ./core/agents/lastfm ./persistence ./tests`. The SQLite dependency emitted a compiler warning, but the tests succeeded.