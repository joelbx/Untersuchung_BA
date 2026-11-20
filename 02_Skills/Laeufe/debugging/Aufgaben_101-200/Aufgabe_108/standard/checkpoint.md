# Cache abstraction task checkpoint

Status: resolved and verified.

Root cause: three modules construct ttlcache directly. ttlcache.Get returns interface{} and ttlcache.GetKeys returns all entries in its map without checking expiration (local module source cache.go). TTL extension differs: HTTP and play tracker disable extension, genre repo leaves the default. The HTTP client also sets a 100-entry size limit and a loader/callback.

Pattern: ttlcache supports per-entry TTL and per-key loader; all three callers use these operations. Hypothesis: one typed adapter with a single no-extension policy and filtered Keys will satisfy the interface while keeping callers typed. A package-private size-limited constructor can preserve HTTP's existing limit.

Reproduction: `GOPROXY=off go test ./utils/cache -run '^TestSimpleCache' -count=1` failed before implementation with `undefined: NewSimpleCache` at simple_cache_test.go:10 and :48, as expected.

Implementation: added generic SimpleCache backed by ttlcache, disabled TTL extension centrally, filtered expired keys, and migrated all three callers. Preserved HTTP's 100-entry limit through a package-private constructor. Added focused tests for typed add/get, TTL, keys, loader caching, loader expiry, and error propagation.

Verification: `GOPROXY=off go test ./utils/cache ./scanner ./core/scrobbler -count=1` passed for all three packages. `git diff --check` passed.

Constraints: local evidence only; no downloads, history/index/harness changes.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.
