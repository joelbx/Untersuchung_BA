# Checkpoint

Issue: Make `getOpenSubsonicExtensions` publicly accessible in the Subsonic router, retain `?f=json`, and return the three existing extensions.

Current finding: `routes()` applies required-parameter and authentication middleware globally before registering the endpoint. The handler already returns `transcodeOffset`, `formPost`, and `songLyrics`.

Completed: Registered the extensions endpoint before the protected middleware chain. Other routes use the same required-parameter, authentication, and last-access middleware through a scoped router. Added a router-level JSON test for both URL forms and the exact extension list, plus a protected-route parameter check.

Verification: `GOPROXY=off GOSUMDB=off go test ./server/subsonic ./server/subsonic/responses` passed. `git diff --check` passed.
