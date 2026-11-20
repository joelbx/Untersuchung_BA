Added `PrioritizedIdentifier` for ISBN and ASIN values, with `stage_import`, identifier-based equality and hashing, and complete JSON serialization. The affiliate queue now checks identifiers for duplicates. Existing `PrioritizedISBN` imports and `isbn=` construction remain supported.

The affiliate server tests pass: **17 passed**.