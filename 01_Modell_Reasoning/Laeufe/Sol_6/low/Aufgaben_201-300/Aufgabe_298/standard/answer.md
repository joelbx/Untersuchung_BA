Implemented opportunistic TTL eviction in `SimpleCache` and added `Values()` so keys and values expose only active entries. Added tests for 10 ms expiration and loader supplied values.

`go test ./utils/cache` passes.