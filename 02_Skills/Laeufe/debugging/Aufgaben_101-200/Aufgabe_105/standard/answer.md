Moved `getOpenSubsonicExtensions` outside the authentication middleware in [api.go](/app/server/subsonic/api.go). Unauthenticated requests with `?f=json` now return the existing JSON response containing exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Added route tests for both URL forms and checked that other routes still require parameters. The Subsonic and response package tests pass.