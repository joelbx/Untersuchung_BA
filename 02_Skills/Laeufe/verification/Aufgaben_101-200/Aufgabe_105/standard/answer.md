Registered `getOpenSubsonicExtensions` outside the authentication group in [api.go](/app/server/subsonic/api.go). The endpoint still supports `?f=json` and returns exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Added coverage for unauthenticated requests to both endpoint paths in [api_test.go](/app/server/subsonic/api_test.go). `go test ./server/subsonic/...` passed.