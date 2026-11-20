# Cache expiration investigation

- Scope: `utils/cache/simple_cache.go` and its relevant tests.
- Repository starts clean at `3993c4d`.
- `rg` is unavailable (`/bin/bash: rg: command not found`); use local `find` and `grep`.
- Status: fixed and verified.
- Baseline: `go test ./utils/cache -run '^TestCache$' -count=1` passed.
- Root cause: `NewSimpleCache` constructs ttlcache but does not run its cleaner; wrapper never invokes `DeleteExpired`. Underlying `Get` checks expiry while `Keys` simply reads stored keys. Thus expired entries remain allocated and appear in `Keys`.
- Local dependency confirms `DeleteExpired` uses an expiration queue; `Items` excludes expired entries. Capacity evicts old entries through ttlcache's existing logic.
- Confirmed approach: track the earliest known expiration in an atomic deadline, run `DeleteExpired` at or after it, and filter entries that expire while enumeration runs.
- Reproduction: `go test ./utils/cache -run '^TestCache$' -ginkgo.focus='evicts expired keys during normal use' -count=1` failed because `Keys()` returned `[expired active]` after 50 ms; expected `[active]`.
- Implemented an atomic pointer holding the earliest known expiry, opportunistic `DeleteExpired`, and `Values`.
- Concurrency reproduction: `go test -race ./utils/cache -run '^TestCache$' -ginkgo.focus='supports concurrent enumeration' -count=1` failed. Stack traces show `ttlcache.Items()` calls `get()` under a read lock while `get()` mutates its LRU list; simultaneous enumerations race. Reassessed enumeration: use `Range` under a wrapper mutex, and keep loader calls outside that mutex.
- Final verification: `go test -race ./utils/cache ./core/scrobbler -count=1 && git diff --check` passed. Also passed non-race `go test ./utils/cache ./core/scrobbler -count=1`.
