Implemented opportunistic expiration cleanup with an atomic eviction deadline and added `Values()` to `SimpleCache`. `Keys()` and `Values()` now return only active entries.

Verification: `go test ./utils/cache` passed.