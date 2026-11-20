Implemented selective SSE delivery. The UI now sends a per-window UUID on its API requests; server middleware stores it in an HttpOnly cookie and request context. The broker uses that context to send user actions only to the same user’s other clients, while background events still broadcast.

`go test ./...`, UI formatting and lint, and `git diff --check` passed. No delegation was used.