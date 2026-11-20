# Checkpoint

Task: Refactor `utils/slice` to use Go 1.23 iterators per Issue #3292.

Completed:
- Removed `BreakUp` and `RangeByChunks`; migrated every production caller to `CollectChunks`.
- Changed `CollectChunks` to take `iter.Seq[T]` then chunk size, allocating a fresh chunk buffer per yield to prevent aliasing.
- Added lazy generic `SeqFunc` and updated slice tests for the new APIs.
- Ran `go test ./utils/slice ./persistence ./scanner ./core`; all passed.
- `git diff --check` passed.
