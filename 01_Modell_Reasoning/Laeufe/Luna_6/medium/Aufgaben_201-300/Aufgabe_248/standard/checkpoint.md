# Checkpoint

Task: Refactor `utils/slice` chunk helpers for Go 1.23 iterators (Issue #3292).

Plan:
- Inspect repository guidance, Go version, utility implementation, and all call sites/tests.
- Remove `BreakUp` and `RangeByChunks`; convert `CollectChunks` to accept `iter.Seq[T]`; add `SeqFunc`.
- Update callers/tests as needed and run relevant existing tests.
