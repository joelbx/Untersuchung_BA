Implemented backward compatibility for legacy string `listenPorts` while moving scanning and reporting to structured `ListenPortStats`. Added `PortStat`, `NewPortStat`, reachability matching, wildcard expansion, and `Package.HasReachablePort`.

Validation passed: `go test ./scan ./models ./report`. The SQLite dependency emitted a compiler warning, but the tests passed.