# Checkpoint

- Task: make `getOpenSubsonicExtensions` public while preserving JSON format and the three required extensions.
- Initial inspection: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and file reads.
- Router: registered `getOpenSubsonicExtensions` before the protected group; the group retains required parameter, authentication, and last-access middleware. Shared form/query parsing remains on the outer router.
- Added an endpoint test for both plain and `.view` paths with no credentials, `?f=json`, and exactly the three required extensions.
- Verification: `GOPROXY=off GOSUMDB=off go test ./server/subsonic/...` exited 0 (Subsonic and responses packages passed; filter has no test files). `git diff --check` exited 0.
