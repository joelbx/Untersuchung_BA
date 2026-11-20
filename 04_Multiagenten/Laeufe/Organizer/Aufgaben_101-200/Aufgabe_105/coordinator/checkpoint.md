# Checkpoint

- Task: make `getOpenSubsonicExtensions` public in the Subsonic router while preserving JSON output and the three advertised extensions.
- Status: complete. Public route is registered before the protected group; all existing protected routes remain in that group.
- Verification: `GOPROXY=off GOSUMDB=off go test ./server/subsonic/...` passed; `git diff --check` passed.
- Delegation: none.
