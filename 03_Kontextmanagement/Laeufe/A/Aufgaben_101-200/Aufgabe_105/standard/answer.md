Moved `getOpenSubsonicExtensions` outside the authentication middleware in [api.go](/app/server/subsonic/api.go). It now serves unauthenticated `?f=json` requests with exactly `transcodeOffset`, `formPost`, and `songLyrics`. Added tests for both endpoint URL forms and for continued protection of `ping`.

The Subsonic and response test suites pass.