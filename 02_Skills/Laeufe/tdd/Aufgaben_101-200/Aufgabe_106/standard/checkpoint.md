# Checkpoint

Task: fix WordPress cache lookup and inactive package filtering in /app.
Status: implementation complete; full suite passed.

Changes:
- WordPress cache is now passed as a map directly. Values are nullable string pointers; `searchCache` returns `("", false)` for a missing key or nil value.
- WordPress scan reads `IgnoreInactive` from the result's server configuration and filters inactive plugins and themes by `Status`.
- Tests cover server setting precedence, active and inactive plugin/theme CVEs, cache hits, misses, and nil entries.

TDD record:
- New scan test failed as expected in both settings: got 4 instead of 2 and 2 instead of 4. It passed after the config fix.
- Cache tests using nullable entries initially failed to compile because the old cache API required `*map[string]string`; they passed after the map type and lookup change.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./wordpress -count=1` passed after the config fix.
- `GOPROXY=off GOSUMDB=off go test ./wordpress ./report -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./...` passed all packages.
- `git diff --check` passed.
- Go emitted an existing compiler warning from `github.com/mattn/go-sqlite3` in `sqlite3-binding.c` (`-Wreturn-local-addr`); no tests failed.
- `rg` was unavailable, so repository searches used `grep` and `find`.
