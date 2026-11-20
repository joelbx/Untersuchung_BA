# Checkpoint

Task: Resolve the PrioritizedISBN limitations in `scripts/affiliate_server.py`.

Completed:
- Added `PrioritizedIdentifier` with generic `identifier`, `stage_import`, priority, and timestamp fields.
- Equality and hashing use only the identifier; queue ordering still uses priority and timestamp.
- JSON serialization now emits identifier, staging flag, priority name, and ISO timestamp.
- Kept `PrioritizedISBN`, the `isbn=` constructor keyword, and `.isbn` property for compatibility; migrated internal queue handling to the generic identifier.

Verification:
- `python -m pytest scripts/tests/test_affiliate_server.py -q` — 16 passed.
- `git diff --check` — passed.
