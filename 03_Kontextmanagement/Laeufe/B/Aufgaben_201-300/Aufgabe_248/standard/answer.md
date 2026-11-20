Issue #3292 is resolved. I removed `BreakUp` and `RangeByChunks`, migrated their callers to Go iterators, changed `CollectChunks` to take the sequence first while keeping yielded chunks independent, and added lazy `SeqFunc` mapping.

The existing tests pass for `utils/slice`, `scanner`, `persistence`, and `core`.