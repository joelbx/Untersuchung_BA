# Checkpoint

- Task: update `scripts/affiliate_server.py` queue elements to support ISBN and ASIN identifiers, identifier-only equality and hashing, staging, and complete JSON serialization.
- Initial repository status: clean.
- Implemented `PrioritizedIdentifier` with identifier-only equality and hashing, priority ordering, staging flag, JSON-safe dictionary output, and a legacy `PrioritizedISBN` wrapper.
- Updated submission, lookup, batching, and status paths to use identifiers and to honor `stage_import`.
- Added focused tests for serialization, deduplication, legacy compatibility, and selective import staging.
- Verification: 35 relevant tests passed; Ruff checks and `git diff --check` passed.
