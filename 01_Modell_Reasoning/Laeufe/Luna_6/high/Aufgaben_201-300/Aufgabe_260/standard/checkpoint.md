# Checkpoint

## Objective
Implement selective SSE event delivery by username and client unique ID, propagate a per-client UUID from the UI through request headers/cookies/context, and update all event call sites and middleware ordering.

## Work plan
1. Inspect request context helpers, constants, router middleware, UI request plumbing, and SSE broker/diode implementations.
2. Implement client ID generation and transport, cookie/context middleware, and logging middleware ordering.
3. Update broker filtering, context-aware sends, event message representation, and diode API usages.
4. Update cookie expiry usages and affected tests/call sites.
5. Run relevant existing tests and summarize results.

## Constraints
Use only repository code and existing tests; do not alter git history, index baseline, or harness configuration.

## Progress
- Added request context helpers and constants for client ID propagation and one-year cookie expiry.
- Added middleware to resolve client IDs from the header/cookie, persist header values in an HttpOnly cookie, and inject the value into context. Reordered middleware and switched request ID logging to `middleware.GetReqID`.
- Added UI UUID generation and header propagation to API, login, and service worker requests.
- Updated the SSE broker to carry sender identity, filter user events by username and client ID, send server events with a background context, and write private wire fields. Renamed diode `set` to `put`.
- Updated event send call sites, authentication username context, and Subsonic cookie expiry usage.
- Verification: `go test ./...` passed; `npm test -- --watchAll=false` passed (11 suites, 41 tests); `git diff --check` passed. Cgo emitted existing TagLib/SQLite compiler deprecation warnings.
