# Checkpoint

Issue resolved: `getOpenSubsonicExtensions` is registered on the root Subsonic router, outside the protected chi group. Existing routes remain in the group with their middleware.

Added tests for unauthenticated JSON responses at both `/getOpenSubsonicExtensions` and `/getOpenSubsonicExtensions.view`, asserting the exact three extensions: `transcodeOffset`, `formPost`, and `songLyrics`.

Checks passed:
- `gofmt -w server/subsonic/api.go server/subsonic/api_test.go`
- `GOPROXY=off GOSUMDB=off go test ./server/subsonic ./server/subsonic/responses`
- `git diff --check`

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); local `grep`/`find` were used for inspection.
