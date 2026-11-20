# Checkpoint

Task: Make `getOpenSubsonicExtensions` public while preserving `?f=json` and the three required extensions.

Completed:
- Added a router-level regression test for anonymous JSON requests to both endpoint paths. It checks status, content type, JSON decoding, and exactly `transcodeOffset`, `formPost`, `songLyrics`.
- Watched `GOPROXY=off GOSUMDB=off go test ./server/subsonic -run '^TestOpenSubsonicExtensionsAllowsAnonymousJSON$' -count=1` fail before the fix with Subsonic error `missing parameter: 'u'`.
- Registered the extension route before the protected route group; retained shared form parsing so the JSON format parameter works.
- Focused test passed after the fix.
- `GOPROXY=off GOSUMDB=off go test ./...` passed after the fix and again after the router refactor.

No blocked checks or known remaining work.
