# Checkpoint

Task: resolve the PrioritizedISBN identifier support, equality, and serialization issue in `scripts/affiliate_server.py`.

Completed:
- Added the `PrioritizedIdentifier` dataclass with a generic identifier, `stage_import`, JSON-safe serialization, identifier-only equality/hash, and priority/timestamp queue ordering.
- Preserved the legacy `PrioritizedISBN` constructor and `.isbn` property for existing callers.
- Carried staging flags through the lookup worker. Products remain cached, while only products requested with staging enabled are added to the import batch.
- Updated queue references and identifier deduplication.

Verification: `python -m pytest scripts/tests/test_affiliate_server.py` passed (16 tests).
