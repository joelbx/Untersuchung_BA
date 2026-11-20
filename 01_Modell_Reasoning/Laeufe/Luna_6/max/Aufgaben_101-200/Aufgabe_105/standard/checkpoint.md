# Checkpoint

Task complete: `getOpenSubsonicExtensions` is registered on the base Subsonic router and can be called without authentication or the usual Subsonic parameter checks. `?f=json` is preserved through the shared response path. All other endpoint registrations retain their parameter checks, authentication, and last-access middleware. The handler still returns exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Verification: `go test ./server/subsonic/...` passed; `gofmt -d server/subsonic/api.go` and `git diff --check` reported no issues.
