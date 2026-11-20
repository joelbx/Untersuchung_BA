Implemented selective event delivery. Request scoped events now reach only other sessions of the same user; server events without a client ID still broadcast to everyone. The UI sends a per-client UUID, and server middleware carries it through an HttpOnly cookie and request context.

Updated the broker, SSE filtering, scanner event contexts, diode API, request logging, and cookie expiry usage. Key changes are in [sse.go](/app/server/events/sse.go), [middlewares.go](/app/server/middlewares.go), [request.go](/app/model/request/request.go), and the UI HTTP client.

Verification passed: `GOPROXY=off go test ./...`, all 41 UI tests, ESLint, Prettier, and `git diff --check`. The Go run emitted existing C compiler warnings; all packages passed.