`getOpenSubsonicExtensions` is now registered outside the authentication middleware. Both route forms support unauthenticated `?f=json` requests and return exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Added route tests. `go test ./server/subsonic ./server/subsonic/responses` and `git diff --check` passed.