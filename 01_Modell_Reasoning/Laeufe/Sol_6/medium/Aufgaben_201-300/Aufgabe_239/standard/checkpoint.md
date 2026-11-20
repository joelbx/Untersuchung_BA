Task: Make user properties and LastFM operations explicitly user scoped.
Status: Completed. User property repositories require explicit user IDs. LastFM session keys and scrobbling use those IDs; authenticated link starts issue single-use callback state.
Verification: GOPROXY=off go test ./core/agents/lastfm ./persistence ./tests; Prettier and ESLint on the changed UI file; git diff --check.
Constraints: Edit checked-out files only; use local code and tests.
