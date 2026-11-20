Refactored `detectScanDest` to return an IP-to-ports map with deduplicated, deterministically ordered ports and an empty map when no ports are found. Updated `execPortsScan` to consume the map.

The focused tests and `go test ./...` pass. The Go toolchain emitted a warning from the bundled `go-sqlite3` C source.