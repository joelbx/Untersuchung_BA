Implemented `singleton.GetInstance[T]` with concrete typed returns, per-type caching, and `sync.Once` initialization. Value and pointer types keep independent instances.

Added tests for repeated retrieval and 20,000 concurrent calls. `go test ./utils/singleton` passes.