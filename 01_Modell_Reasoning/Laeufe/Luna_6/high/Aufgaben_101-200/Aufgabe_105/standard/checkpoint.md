# Checkpoint

Implemented public routing for `getOpenSubsonicExtensions` in `server/subsonic/api.go`. The outer router keeps form parsing and registers the capability endpoint directly; existing routes are mounted under a separate router with required-parameter checks, authentication, and access tracking. This allows the public endpoint to work without credentials and keeps query/form `f=json` processing.

Added an API route test asserting unauthenticated JSON access, JSON content type, and exactly `transcodeOffset`, `formPost`, and `songLyrics`.

Verification: `go test ./server/subsonic` passed; `git diff --check` passed.
