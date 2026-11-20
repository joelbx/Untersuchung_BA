Removed `BreakUp` and `RangeByChunks` and migrated their callers to Go iterators. `CollectChunks` now accepts the sequence first and reuses a buffer while yielding independent chunks. Added lazy `SeqFunc` and regression tests.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./...` passed.