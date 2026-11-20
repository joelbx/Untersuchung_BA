# Checkpoint

Issue #3292 implementation completed in `/app`.

- Removed `BreakUp` and `RangeByChunks`; migrated all production call sites to Go 1.23 `slices.Chunk`.
- Updated `CollectChunks` to accept an `iter.Seq[T]` followed by the chunk size. It reuses a buffer and clones yielded chunks to avoid backing-array aliasing.
- Added `SeqFunc` as a lazy mapping iterator over a slice.
- Updated the existing tests and playlist parser for the new `CollectChunks` signature.
- Verification passed: `go test ./utils/slice ./core ./scanner ./persistence`.
