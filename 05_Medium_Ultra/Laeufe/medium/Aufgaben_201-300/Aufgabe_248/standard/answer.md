Removed `BreakUp` and `RangeByChunks`, changed `CollectChunks` to accept a sequence first and yield independent chunks, and added the lazy `SeqFunc` mapper. Updated all repository call sites.

The existing tests pass for `utils/slice`, `persistence`, `scanner`, and `core`.