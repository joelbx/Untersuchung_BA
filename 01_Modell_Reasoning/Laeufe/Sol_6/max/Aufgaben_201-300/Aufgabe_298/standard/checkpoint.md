# SimpleCache expiration fix

Status: complete.

Changes: an atomic eviction deadline limits global expiration sweeps to once per 10 milliseconds. `Keys` and `Values` return active entries, and inserts at capacity clear expired entries before evicting an active item. Loader inserts also perform eviction.

Verification: `GOPROXY=off GOSUMDB=off go test ./utils/cache -count=1`, `go test -race ./utils/cache -count=1`, and `go test ./core/scrobbler ./scanner -count=1` passed. One existing cache spec remains pending. `git diff --check` passed.
