VERDICT: FIX

**Code defect:** [simple_cache.go](/app/utils/cache/simple_cache.go:71) clears `evictionDeadline` before deleting expired entries. A concurrent `AddWithTTL` can then skip eviction and insert into a full cache while an expired entry still occupies capacity, potentially evicting an active entry. Keep the sweep synchronized with insertion, or keep a due deadline visible until deletion finishes.

**Tests run:** `GOPROXY=off GOSUMDB=off go test ./utils/cache -count=1`, `GOPROXY=off GOSUMDB=off go test -race ./utils/cache -count=1`, and `GOPROXY=off GOSUMDB=off go test ./core/scrobbler -count=1` all passed. The interleaving above is not covered by those tests. No `TEST_ENVIRONMENT_PROBLEM`.