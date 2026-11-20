Implemented explicit user scoping for all `UserPropsRepository` operations. The SQL repository uses only the supplied user ID, and the mock stores values by `(userID, key)`.

LastFM session key reads, writes, and deletes now receive a user ID. Agent operations use their user ID, while link status, unlink, and the authorization callback use the authenticated request user. The UI callback no longer sends a user ID query parameter.

Verification passed: `go test ./persistence ./core/agents/lastfm` and `git diff --check`.