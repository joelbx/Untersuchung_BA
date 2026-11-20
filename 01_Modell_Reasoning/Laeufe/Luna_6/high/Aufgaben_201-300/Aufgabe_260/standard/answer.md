Implemented selective SSE delivery. User action events now reach other sessions for the same user while excluding the originating client; server wide refreshes and keepalives still broadcast.

Added client UUID propagation through UI requests, server cookie and context middleware, and request scoped event contexts. Updated broker sends, diode naming, logging, and cookie expiry usage.

Verification passed: `go test ./...`, UI tests (11 suites, 41 tests), and `git diff --check`. The Go build emitted existing TagLib and SQLite compiler warnings.