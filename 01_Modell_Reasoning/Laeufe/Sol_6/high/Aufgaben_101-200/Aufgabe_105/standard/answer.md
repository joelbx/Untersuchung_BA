Moved `getOpenSubsonicExtensions` outside the authentication and required-parameter middleware in [api.go](/app/server/subsonic/api.go:69). Its `?f=json` response remains available without credentials and contains exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Added route tests in [api_test.go](/app/server/subsonic/api_test.go:114). The Subsonic and response test suites pass.