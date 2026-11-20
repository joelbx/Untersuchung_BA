# Checkpoint

- Task: make `getOpenSubsonicExtensions` public while preserving `?f=json` and its three advertised extensions.
- Found: `server/subsonic/api.go` applies `authenticate` and `checkRequiredParameters` at the root router, so moving the endpoint out of its current `r.Group` alone will not make it public.
- Completed: registered the extensions route on the root router and scoped required parameter, authentication, and last access middleware to all other routes.
- Added a route test for both endpoint URL forms, unauthenticated JSON output, the exact three extensions, and a protected route's parameter check.
- Verification: `GOPROXY=off GOSUMDB=off go test ./server/subsonic/...` passed; `git diff --check` passed.
