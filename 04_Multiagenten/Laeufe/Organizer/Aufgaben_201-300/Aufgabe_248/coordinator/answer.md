Removed `BreakUp` and `RangeByChunks` and migrated their callers to Go 1.23’s `slices.Chunk`. `CollectChunks` now accepts `(iter.Seq[T], size)`, reuses a collection buffer, and yields independent chunks. Added the lazy `SeqFunc` mapper and tests.

The relevant tests passed: `go test ./utils/slice ./core ./scanner ./persistence`. No delegation was used.