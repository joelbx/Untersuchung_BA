`getOpenSubsonicExtensions` is now registered on the public router, outside the protected middleware. Shared form parsing preserves `?f=json`.

Added a route test for unauthenticated JSON access and the exact three extensions: `transcodeOffset`, `formPost`, and `songLyrics`.

Verification passed: `go test ./server/subsonic` and `git diff --check`.