Removed `BreakUp` and `RangeByChunks`, migrated their callers to Go 1.23 iterators, and added lazy `SeqFunc` in [slice.go](/app/utils/slice/slice.go). `CollectChunks` now takes `(seq, size)`, reuses a buffer, and yields independent chunks.

Tests passed for `utils/slice`, `persistence`, `core`, and `scanner`.