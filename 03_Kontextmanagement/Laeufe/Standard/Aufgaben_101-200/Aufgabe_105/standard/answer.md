Moved `getOpenSubsonicExtensions` outside the authentication middleware in [api.go](/app/server/subsonic/api.go). It remains available at both Subsonic URL forms and returns JSON with exactly `transcodeOffset`, `formPost`, and `songLyrics` when called with `?f=json`.

Added route coverage in [api_test.go](/app/server/subsonic/api_test.go). The Subsonic and response tests pass.