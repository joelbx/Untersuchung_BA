Moved `getOpenSubsonicExtensions` outside the authentication middleware in [api.go](/app/server/subsonic/api.go). Added a request test confirming that an unauthenticated `?f=json` call returns JSON with exactly `transcodeOffset`, `formPost`, and `songLyrics`.

`go test ./server/subsonic/...` passes.