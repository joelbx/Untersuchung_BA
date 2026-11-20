# Checkpoint

Implemented selective SSE event delivery in `/app`:

- Added client unique ID context helpers, header/cookie constants, and middleware that resolves the header or cookie and writes a one year HttpOnly cookie for header values.
- Registered the middleware before logging; logging now uses `middleware.GetReqID`.
- Added a persistent browser client UUID and sent it from login and the shared API HTTP client.
- Changed event publishing to carry the sender context, filtered subscribers by client ID and username, and used background contexts for keepalives and scanner-wide refreshes.
- Renamed diode `set` to `put`, made SSE message fields unexported, updated server start delivery, and replaced the Subsonic cookie expiry constant.

Verification: `go test ./server/events ./server ./server/subsonic ./scanner` passes. `git diff --check` passes. The C++ TagLib dependency emits a pre-existing deprecation warning during Go test builds.
