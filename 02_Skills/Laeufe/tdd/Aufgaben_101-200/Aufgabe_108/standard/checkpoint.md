# Cache abstraction work

Status: implemented typed `utils/cache.SimpleCache[V]` over `ttlcache`, migrated the HTTP client, genre repository, and play tracker, and added cache behavior tests. The wrapper keeps TTL fixed on reads, filters expired keys, and supports nil interface values. The HTTP client retains its 100-entry size limit.

TDD: `GOPROXY=off go test ./utils/cache -run '^TestSimpleCache' -count=1` initially failed with `undefined: NewSimpleCache`, then passed after implementation. The size-limit test initially failed with `undefined: newSimpleCacheWithSizeLimit`, then passed. The nil-interface test initially panicked on `interface conversion: interface is nil, not interface {}`, then passed after storing boxed values.

Verification: `GOPROXY=off go test ./utils/cache ./scanner ./core/scrobbler -count=1` passed. `git diff --check` passed.

Full suite: `GOPROXY=off go test ./...` exited 1. All changed packages passed. The only failing package was `github.com/navidrome/navidrome/scanner/metadata/taglib`: the specs `Correctly parses m4a (aac) gain tags` and `Correctly parses m4a (aac) gain tags (uppercase)` at `scanner/metadata/taglib/taglib_test.go:157-158` failed because `replaygain_album_gain` contained `["0.37", "0.37"]` where the test expected `["0.37"]`. This package was not changed by the cache work. Its two access-forbidden specs were pending.

An earlier focused run failed in the new TTL test because a middle read happened after its 80 ms deadline under concurrent load. The test now uses a 300 ms TTL and wider timing window; focused and full-suite runs passed the cache package afterward.

Environment: `rg` is unavailable (`/bin/bash: line 1: rg: command not found`); using `grep` and `find` for local inspection.
