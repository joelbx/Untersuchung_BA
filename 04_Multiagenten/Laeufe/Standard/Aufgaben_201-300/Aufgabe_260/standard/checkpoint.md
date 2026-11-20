Task: Selective SSE delivery for same-user sessions excluding originating client.
Status: Implemented and verified.
Changes: Client UUID headers in UI; header/cookie/context middleware; contextual broker filtering; updated queue and event API, call sites, cookie lifetime, logging; focused middleware and broker tests.
Verification: go test ./server/events ./server ./server/subsonic ./scanner passed; UI 11 suites/41 tests passed; Prettier and git diff --check passed.
