`getOpenSubsonicExtensions` is now registered outside the authentication middleware in [api.go](/app/server/subsonic/api.go). It remains available without credentials and returns JSON for `?f=json` with exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Added route coverage in [api_test.go](/app/server/subsonic/api_test.go). `GOPROXY=off GOSUMDB=off go test ./server/subsonic/...` passed.