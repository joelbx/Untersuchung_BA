# Checkpoint

Objective: make `getOpenSubsonicExtensions` publicly accessible in `server/subsonic/api.go`, preserve `?f=json` output, and ensure the response advertises exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Completed:
- Scoped required-parameter validation, authentication, and last-access middleware to protected Subsonic routes.
- Kept form parsing on the router and registered `getOpenSubsonicExtensions` outside the protected group.
- Added route-level coverage for a credential-free `?f=json` request and the exact extension list.
- `go test ./server/subsonic` passes.
