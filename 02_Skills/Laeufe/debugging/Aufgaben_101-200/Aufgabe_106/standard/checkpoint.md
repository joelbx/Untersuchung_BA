# Checkpoint

Phase 1: `searchCache` accepts `*map[string]string` and dereferences it. Its value type cannot represent a nil entry. `FillWordPress` uses global `Conf.WpIgnoreInactive`, while report detection and result filtering use `Conf.Servers[r.ServerName].WordPress.IgnoreInactive`. The existing `removeInactives` helper correctly checks `Status == "inactive"`; the configuration mismatch prevents it from running as expected. No local WordPress changes preceded this task (`git diff` empty).

Phase 2: `FilterInactiveWordPressLibs` already reads the per-server setting and checks `Status`; this is the working reference. Cache writers and the report caller all use the same map, so the value type and signature need coordinated updates to support nil values and direct map lookup.

Phase 3 hypothesis: Passing a map directly and using nullable string values will allow a hit/miss result for both absent and nil entries; reading the per-server flag in `FillWordPress` will cause inactive themes and plugins to be skipped while retaining active ones. Regression tests will verify both before the fix.

Phase 4: Added regression tests before the fix. `GOPROXY=off GOSUMDB=off go test ./wordpress -run 'TestSearchCacheNilValue|TestFillWordPressUsesServerIgnoreInactive' -count=1` failed as expected because `searchCache` and `FillWordPress` accepted `*map[string]string` and could not represent nil entries. Updated cache storage and lookup to `map[string]*string`, with absent or nil entries returning `("", false)`, and changed `FillWordPress` to use per-server `IgnoreInactive`. The existing `removeInactives` status check now runs under that setting. Added tests for empty non-nil values, inactive themes and plugins, active plugins, and the setting in both directions.

Final verification: `GOPROXY=off GOSUMDB=off go test ./wordpress ./models ./report && git diff --check` exited 0. The only output besides passing packages was an existing compiler warning from sqlite3-binding.c; no test failed. `rg` was unavailable, so repository searches used grep/find. No downloads were attempted.
