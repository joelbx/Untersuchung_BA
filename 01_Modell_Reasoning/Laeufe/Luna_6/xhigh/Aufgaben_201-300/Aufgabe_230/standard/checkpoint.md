# Checkpoint

Task: Resolve the PrioritizedISBN identifier handling and serialization issue in `scripts/affiliate_server.py`.

Completed:
- Added `PrioritizedIdentifier` with generic identifier, stage_import, priority, and timestamp fields.
- Implemented identifier-only equality/hash and priority/timestamp queue ordering.
- Added complete JSON-safe serialization and retained the legacy `PrioritizedISBN` constructor/property compatibility.
- Kept stage_import metadata through batch lookup and filtered import staging accordingly.
- Updated queue duplicate detection to compare identifiers.

Validation: `pytest -q scripts/tests/test_affiliate_server.py` passed (16 tests).
