# Checkpoint

Task: Replace PrioritizedISBN with a generic queue identifier supporting ISBN and ASIN, stage_import, identifier-based equality/hash, and complete API serialization.

Plan: inspect local callers and tests; write a failing regression test; implement the smallest compatible change; run focused and project tests.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); using grep/find.

## Result

Implemented `PrioritizedIdentifier` with generic identifier, import staging flag, identifier-only equality and hash, queue ordering, and JSON-safe `to_dict()` fields. Kept `PrioritizedISBN` as a compatibility alias with the `isbn` keyword/property. Queue submission now compares queue elements, and batch processing honors `stage_import` while caching all fetched products.

Tests were written before implementation. The new class tests failed because `PrioritizedIdentifier` was missing. The staging test failed before implementation because the API received queue objects instead of identifier strings.

Checks:
- `pytest -q scripts/tests/test_affiliate_server.py`: 20 passed.
- `pytest -q scripts --ignore=scripts/tests/test_isbndb.py --ignore=scripts/tests/test_partner_batch_imports.py`: 40 passed.
- `ruff check scripts/affiliate_server.py scripts/tests/test_affiliate_server.py`: passed; existing pyproject deprecation warning.
- `git diff --check`: passed.

Full-suite limitations:
- `pytest -q` failed during collection with `ValueError: Plugin name already registered: /app/infogami/conftest.py` (module `infogami.conftest`). No tests were collected.
- `pytest -q scripts` reported 40 passed and two collection errors, `scripts/tests/test_isbndb.py` and `scripts/tests/test_partner_batch_imports.py`, caused by `requests.exceptions.ProxyError` while fetching a schema from `raw.githubusercontent.com` (`Tunnel connection failed: 403 Forbidden`). Their results remain unknown offline. No dependency download attempted.
