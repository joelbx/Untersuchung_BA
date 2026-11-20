Refactored the slice utilities for Go 1.23 iterators. Removed `BreakUp` and `RangeByChunks`, migrated their callers, changed `CollectChunks` to accept the sequence first and yield independent chunks, and added lazy `SeqFunc`.

The existing tests passed for `utils/slice`, `scanner`, `persistence`, and `core`.