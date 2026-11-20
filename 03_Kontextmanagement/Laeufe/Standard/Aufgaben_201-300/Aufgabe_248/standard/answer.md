Refactored the slice utilities to use Go iterators. Removed `BreakUp` and `RangeByChunks`, changed `CollectChunks` to accept a sequence first, and added lazy `SeqFunc` mapping. Migrated all callers and updated the tests.

Relevant tests passed for `utils/slice`, `persistence`, `scanner`, and `core`.