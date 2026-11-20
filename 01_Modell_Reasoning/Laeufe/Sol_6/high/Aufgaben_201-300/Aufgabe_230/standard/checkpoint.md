# Checkpoint

Task: expand affiliate queue identifiers, equality, and serialization.

Status: completed implementation and verification.

Changes:
- Added PrioritizedIdentifier with generic identifier, stage_import, identifier-only equality/hash, and complete JSON-ready to_dict.
- Preserved PrioritizedISBN constructor compatibility and ISBN property.
- Updated submit, lookup, status, and batch processing to use identifiers and honor import staging.
- Added tests for serialization, deduplication, legacy construction, queue behavior, and selective staging.

Verification:
- pytest -q scripts/tests/test_affiliate_server.py: 20 passed.
- ruff check scripts/affiliate_server.py scripts/tests/test_affiliate_server.py: passed.
- git diff --check: passed.
