The existing patch addresses the issue, and the independent review identified no code defects. No code changes were needed in this correction round.

The Go tests for `internal/config` and `internal/cmd` passed, as did `git diff --check`.

**TEST_ENVIRONMENT_PROBLEM:** Both UI commands, `npm test -- --runInBand --watch=false` and `npm run build`, exited 127 because `npm` is unavailable. The UI checks remain unverified.