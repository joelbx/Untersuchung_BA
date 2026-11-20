`getOpenSubsonicExtensions` is now registered outside the authentication and required-parameter middleware in [api.go](/app/server/subsonic/api.go). A request test confirms that both endpoint paths accept unauthenticated `?f=json` requests and return exactly `transcodeOffset`, `formPost`, and `songLyrics`.

`go test ./server/subsonic ./server/subsonic/responses` passed.