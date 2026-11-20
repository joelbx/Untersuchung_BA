Removed `BreakUp` and `RangeByChunks` and migrated their callers to Go iterators. `CollectChunks` now takes the sequence first, reuses an internal buffer, and yields independent chunks. Added lazy `SeqFunc` in [slice.go](/app/utils/slice/slice.go).

Tests passed for `utils/slice`, `core`, `scanner`, and `persistence`.