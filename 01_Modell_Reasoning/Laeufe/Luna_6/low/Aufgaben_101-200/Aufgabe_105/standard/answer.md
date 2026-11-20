`getOpenSubsonicExtensions` now bypasses required user parameters and authentication while using the existing response formatter, preserving `?f=json`. The handler returns exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Relevant tests passed: `go test ./server/subsonic/...`.