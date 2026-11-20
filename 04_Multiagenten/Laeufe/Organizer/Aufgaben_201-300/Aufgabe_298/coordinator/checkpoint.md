Task: Fix SimpleCache expiration, opportunistic eviction, Values, loader behavior, and size/TTL correctness.
Status: Implemented and verified. No delegation used.
Changes: atomic eviction deadline and expiration sweep; active-only Keys/Values; eviction around adds and loader insertion; capacity cleanup; TTL and loader tests.
Tests: GOPROXY=off go test ./utils/cache; GOPROXY=off go test ./core/scrobbler ./scanner; git diff --check.
