`getOpenSubsonicExtensions` is now registered outside the authentication middleware in [api.go](/app/server/subsonic/api.go). Unauthenticated requests with `?f=json` return JSON containing exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Route tests cover both URL forms and confirm a protected endpoint still requires parameters. `go test ./server/subsonic` passed.