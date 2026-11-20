# Checkpoint

Task: implement selective SSE event delivery for the originating user/client in `/app`.

Implemented:
- Added `UIClientUniqueIDHeader`, `CookieExpiry`, `WithClientUniqueId`, and `ClientUniqueIdFrom`.
- Added middleware to set/reuse the HttpOnly client ID cookie and put the ID in request context; registered it before request logging. The request ID logger uses `middleware.GetReqID`.
- Generated one UUID per UI page instance and attached it to shared API calls, login, and the service worker check. EventSource receives the ID cookie established by the keepalive request.
- Made broker sends context-aware, filtered request events to the same user's other client sessions, and kept background events global. Renamed diode `set` to `put` and made message fields private.
- Passed request contexts for rating, starring, scrobbling, and scan progress; scan-wide refreshes and keepalives use `context.Background()`.
- Replaced Subsonic's local cookie expiry with `consts.CookieExpiry`. Added coverage for cookie handling and event filtering.

Verification:
- Full `go test ./...` passed; the TagLib and SQLite C compiler emitted existing deprecation/compiler warnings.
- A final `go test ./server/... ./scanner/...` passed after the last Go edit.
- `npm test -- --watchAll=false --runInBand` passed (11 suites, 41 tests).
- `npm run lint` passed.
- `npm run build` was attempted but this repository's Webpack 4 build fails on Node 20 with `ERR_OSSL_EVP_UNSUPPORTED` before completing.
