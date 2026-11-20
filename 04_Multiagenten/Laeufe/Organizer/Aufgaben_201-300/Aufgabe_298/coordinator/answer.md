Implemented opportunistic expiration cleanup in `SimpleCache` using an atomic eviction deadline. `Keys` and the new `Values` method return only active entries; adds and loader insertions clear expired entries before capacity eviction.

Tests passed: `go test ./utils/cache ./core/scrobbler ./scanner`. No delegation was used.