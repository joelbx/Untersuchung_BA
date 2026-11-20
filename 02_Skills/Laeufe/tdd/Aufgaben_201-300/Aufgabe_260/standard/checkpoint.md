# Checkpoint

Task: selective event delivery by user and client.
Status: implemented and verified.

Changes: UI sends a per-window UUID header on API and login requests. Middleware sets/reuses an HttpOnly one-year cookie and injects the ID into request context. Broker messages carry sender identity, omit the origin client and other users when scoped, and broadcast when no client ID is present. Scanner progress uses sender context; forced library refresh and keepalives use background context. Diode `set` renamed `put`; message fields made private. Cookie expiry and request logging updated.

TDD: new broker, middleware, scanner progress, and UI header tests were run failing before the corresponding implementation, then passing.

Verification: `go test ./...` passed (with existing C compiler warnings from go-sqlite3 and TagLib); `CI=true npm test -- --watch=false --runInBand` passed (12 suites, 42 tests); `npm run lint` passed; changed UI files passed Prettier check; `git diff --check` passed.

Tooling note: `rg` is unavailable; repository searches used `find` and `grep`. No required check was blocked.
