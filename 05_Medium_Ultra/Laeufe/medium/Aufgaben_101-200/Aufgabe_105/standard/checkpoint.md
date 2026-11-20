# Checkpoint

Issue: make `getOpenSubsonicExtensions` public while preserving JSON output and its three extensions.

Initial finding: `server/subsonic/api.go` applies authentication at the root router, including this endpoint. The endpoint data already lists `transcodeOffset`, `formPost`, and `songLyrics`.

Completed: registered the extension endpoint on the outer router and placed all other endpoints inside a group with required-parameter checks, authentication, and last-access updates. Added route tests for unauthenticated JSON responses at both endpoint paths, the exact three extensions, and protected-route checks.

Verification: `GOPROXY=off GOSUMDB=off go test ./server/subsonic ./server/subsonic/responses` passed. `git diff --check` passed.
