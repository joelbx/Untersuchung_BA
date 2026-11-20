Implementer progress: verifying the reported ttlcache callers and their tests. Will add the typed cache interface, migrate callers, and run local tests. External research is off limits.
Verified three direct ttlcache callers. Implemented a typed, mutex-protected cache with lazy TTL expiry and an internal size limit for HTTP. Migrated callers; next step is tests and review.
Relevant package tests pass for cache, scrobbler, and scanner. Removed the now-unused ttlcache module entries. Final verification in progress.
Final verification: uncached tests for ./utils/cache ./core/scrobbler ./scanner passed with GOPROXY=off; git diff --check passed. Patch contains typed cache, migrated callers, focused tests, and dependency cleanup.
