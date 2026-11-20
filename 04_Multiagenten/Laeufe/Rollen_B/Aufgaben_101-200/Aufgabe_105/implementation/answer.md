`getOpenSubsonicExtensions` is now registered outside the authentication middleware in [api.go](/app/server/subsonic/api.go). It remains available without credentials on both URL forms, and `?f=json` returns exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Route tests were added in [api_test.go](/app/server/subsonic/api_test.go). `go test ./server/subsonic -count=1` passes.