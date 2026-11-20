Task: Move user-specific properties to user_props with context-scoped repository; migrate LastFM session key.
Status: Complete. Added user_props migration (including legacy LastFM session key copy), model/DataStore interface, SQL repository, LastFM refactor, request ID error logging, mock support, and repository tests.
Verification: GOPROXY=off GOTOOLCHAIN=local go test ./persistence ./core/agents/lastfm ./db/migration; GOPROXY=off GOTOOLCHAIN=local go test ./core/scrobbler ./server/... ./tests/...; git diff --check. All passed.
