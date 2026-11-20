Task: Add user-scoped property storage and refactor Last.fm session keys.
Status: Complete. Added user_props migration with Last.fm legacy key transfer, model/DataStore interface and SQL repository, Last.fm integration and contextual request ID logs, mock support, and repository isolation test.
Verification: go test ./persistence ./core/agents/lastfm ./tests; go test ./...; git diff --check. All passed.
Constraints: Used local code and tests only; did not change git history, index baseline, or harness configuration.
