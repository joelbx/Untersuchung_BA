# Checkpoint

Issue: expired SimpleCache entries persisted in memory and appeared in key lists.
Status: implementation complete.
Changes: added deadline scheduled opportunistic eviction with an atomic pointer; evict before writes and reads; added active-only Keys and Values; schedule TTLs for loaded values; added expiration, capacity, and loader tests.
Verification: `go test ./utils/cache`, `go test -race ./utils/cache`, and `go test ./core/scrobbler` passed with `GOTOOLCHAIN=local GOPROXY=off`. `git diff --check` passed.
