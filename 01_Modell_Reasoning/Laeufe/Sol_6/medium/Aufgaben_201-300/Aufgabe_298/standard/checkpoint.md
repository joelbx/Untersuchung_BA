# Cache eviction checkpoint

- Task: make `simpleCache` evict expired entries during normal operations and expose active values.
- Status: implemented atomic deadline based opportunistic eviction, active `Keys`/`Values`, and loader TTL handling; added focused cache tests.
- Validation: `go test ./utils/cache`, `go test -race ./utils/cache`, and `go test ./core/scrobbler` pass with `GOPROXY=off GOSUMDB=off`. `git diff --check` passes.
