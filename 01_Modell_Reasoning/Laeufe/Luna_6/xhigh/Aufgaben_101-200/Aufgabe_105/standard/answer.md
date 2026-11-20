Registered `getOpenSubsonicExtensions` outside the protected middleware group. Form parsing remains enabled, and the handler returns JSON for `?f=json`. The route test verifies access without credentials or other Subsonic parameters and checks for exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Validation: `go test ./server/subsonic` passed.

Changes are in [api.go](/app/server/subsonic/api.go:69) and [api_test.go](/app/server/subsonic/api_test.go:16).