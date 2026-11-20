# Checkpoint

Task: Fix SimpleCache expiration, opportunistic eviction, Values, loader and capacity behavior with test-driven development.

Implemented: atomic-pointer throttled expiration sweeps, active-only Keys/Values, eviction before capacity-limited insertions, and loader path eviction. Added regression tests for 10 ms expiration, loader values/TTL, and capacity with an expired newer item. Behavioral tests were observed failing before implementation; the initial Values API test produced the expected missing-method compile error before the API was added.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./utils/cache -count=1` passed after final test timing adjustment.
- `git diff --check` passed.
- `GOPROXY=off GOSUMDB=off go test ./...` exited 1. `scanner/metadata/taglib` failed two existing m4a AAC gain-tag cases: `Correctly parses m4a (aac) gain tags` and `Correctly parses m4a (aac) gain tags (uppercase)` at `taglib_test.go:98`; actual `replaygain_album_gain` contains duplicate `0.37` values, expected one. Cache package and cache consumers passed. No files in taglib were changed.

Tooling: `rg` unavailable; used local `find`/`grep`. No downloads.
