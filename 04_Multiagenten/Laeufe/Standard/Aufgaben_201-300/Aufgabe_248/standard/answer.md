Removed `BreakUp` and `RangeByChunks`, migrated their callers to the sequence-based `CollectChunks`, and added lazy `SeqFunc`. `CollectChunks` reuses its collection buffer while copying yielded chunks so they remain independent.

The existing tests passed for `utils/slice`, `scanner`, `persistence`, and `core`.