Removed `BreakUp` and `RangeByChunks`, migrated their callers to the sequence-based `CollectChunks` API, and added lazy `SeqFunc`. `CollectChunks` reuses an internal buffer and copies yielded chunks so retained chunks stay independent.

Verification passed: tests for `utils/slice`, `scanner`, `persistence`, and `core`; formatting and diff checks; and a Go-source search for the removed APIs.