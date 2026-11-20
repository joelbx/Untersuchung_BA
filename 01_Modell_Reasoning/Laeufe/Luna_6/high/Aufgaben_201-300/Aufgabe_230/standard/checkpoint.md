# Checkpoint

Task: Resolve the PrioritizedISBN limitations in `scripts/affiliate_server.py`.

Implemented:
- Added `PrioritizedIdentifier` with generic `identifier`, `stage_import`, `priority`, and timestamp fields.
- Equality and hashing use only `identifier`; queue ordering remains priority then timestamp.
- `to_dict()` emits JSON-compatible identifier, staging flag, priority name, and ISO timestamp fields.
- Kept `PrioritizedISBN` and the `isbn` constructor/property as compatibility aliases.
- The batch lookup now honors `stage_import` when deciding which returned products enter the import batch.

Verification: `python -m pytest scripts/tests/test_affiliate_server.py -q` passed (16 tests).
