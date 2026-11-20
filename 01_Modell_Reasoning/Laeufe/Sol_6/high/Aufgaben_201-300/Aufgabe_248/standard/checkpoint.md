# Issue 3292 checkpoint

- Removed `BreakUp` and `RangeByChunks` from `utils/slice/slice.go` and migrated all repository callers.
- `CollectChunks` now accepts `(iter.Seq[T], int)`, reuses its collection buffer, and clones yielded chunks to keep them independent.
- Added lazy `SeqFunc` and used it to stream play queue track IDs.
- Verified with `go test ./utils/slice ./core ./scanner ./persistence` and `git diff --check`.
