# Cache expiration fix checkpoint

- Task: make `simpleCache` evict expired entries during normal operations, expose active values, and preserve loader, TTL, and size behavior.
- Initial state: repository clean; implementation and tests located in `utils/cache`.
- Implemented atomic next-expiration tracking, opportunistic sweeps, active `Keys`/`Values`, and loader insertion through the normal cache path.
- Updated `playTracker` to read active values directly; added short-TTL, loader, capacity, and expired-player coverage.
- Verification: `go test -count=1 ./utils/cache ./core/scrobbler` passed; `go test -race ./utils/cache` passed; `git diff --check` passed.
