# Checkpoint

Objective: Introduce a generic `utils/cache.SimpleCache[V]`, migrate direct `ttlcache` usage to the internal abstraction where appropriate, and run relevant existing tests.

Status: Implemented `SimpleCache[V]` with typed entries, expiration, loader support, and active key listing. Migrated the HTTP client, cached genre repository, and play tracker; retained the HTTP client's 100 entry limit and removed the unused `ttlcache` dependency. `gofmt`, `git diff --check`, and `go test ./utils/cache ./scanner ./core/scrobbler` pass.
