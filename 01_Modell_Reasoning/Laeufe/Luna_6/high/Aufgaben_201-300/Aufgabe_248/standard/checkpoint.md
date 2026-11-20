# Checkpoint

Task: Modernize `utils/slice` chunking helpers for Go 1.23 iterators.

Completed:
- Removed `BreakUp` and `RangeByChunks` and migrated their repository call sites to iterator based chunking.
- Changed `CollectChunks` to accept `(iter.Seq[T], chunkSize)` and reuse its collection buffer while cloning emitted chunks to avoid aliasing.
- Added `SeqFunc` and tests for lazy mapping and independent emitted chunks.

Verification: `go test ./utils/slice ./scanner ./core` passed. `git diff --check` passed.
