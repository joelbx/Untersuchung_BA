# Checkpoint
Task: selective SSE delivery by user and client.
Completed: UI per-window UUID header on fetch and login; server header/cookie/context middleware; broker context-based filtering; request-scoped event calls; background refresh/keepalive; diode put rename; unexported messages; shared cookie expiry; focused tests.
Verification: `go test ./...`, `CI=true npm run check-formatting`, `CI=true npm run lint`, and `git diff --check` passed.
Delegation: none.
