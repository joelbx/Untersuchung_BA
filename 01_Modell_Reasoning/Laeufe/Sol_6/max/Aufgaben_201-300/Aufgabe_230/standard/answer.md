Added `PrioritizedIdentifier` for ISBNs and ASINs, with `stage_import`, identifier-only equality and hashing, and complete JSON-compatible serialization. Updated queue deduplication and batch staging while preserving the `PrioritizedISBN` constructor and legacy string inputs.

Verification: 37 affiliate and vendor tests passed; Ruff and `git diff --check` passed.