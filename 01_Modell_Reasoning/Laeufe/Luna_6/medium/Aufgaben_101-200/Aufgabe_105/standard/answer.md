`getOpenSubsonicExtensions` is now registered outside authentication middleware. Its handler still uses the existing response serializer, which supports `?f=json`, and returns the three required extensions: `transcodeOffset`, `formPost`, and `songLyrics`.

Verified with `go test ./server/subsonic/...`.