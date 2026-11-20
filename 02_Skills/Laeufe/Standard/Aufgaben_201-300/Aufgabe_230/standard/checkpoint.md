# Checkpoint

Task: Expand affiliate queue items to generic identifiers, with staging control, identifier-based equality, and complete JSON serialization.

Status: implemented in `scripts/affiliate_server.py`, with focused tests in `scripts/tests/test_affiliate_server.py`.

Changes:
- Added `PrioritizedIdentifier` dataclass for ISBN/ASIN values, with `identifier`, `stage_import`, priority, and timestamp.
- Equality and hashing use only the identifier; queue ordering uses priority then timestamp.
- JSON dictionary contains identifier, staging flag, priority name, and ISO timestamp.
- Kept `PrioritizedISBN`, its `isbn` constructor keyword, and its read-only `isbn` attribute as compatibility aliases.
- Submit checks queued item equality; batch processing honors `stage_import` while caching all returned products.

Checks:
- `pytest -q scripts/tests/test_affiliate_server.py`: 18 passed.
- `git diff --check`: passed.
- `python -m compileall -q scripts/affiliate_server.py scripts/tests/test_affiliate_server.py`: passed.
- Re-ran `pytest -q scripts/tests/test_affiliate_server.py` and `git diff --check` after positional constructor compatibility change: 18 passed; diff check passed.
