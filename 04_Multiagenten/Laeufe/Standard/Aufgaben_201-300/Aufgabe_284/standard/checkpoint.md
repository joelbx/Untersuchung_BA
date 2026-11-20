Task: Consolidate reversetunnel server local site and reuse its existing proxy access point/cache.
Status: Complete. The server owns one localSite, validates local service connections against it, and reuses the proxy's existing access point and clients. Updated focused tests.
Verification: `go test ./lib/reversetunnel -count=1` passed; `git diff --check` passed.
Constraints: Do not alter git history, index baseline, or harness configuration. Use local code and existing tests only.
