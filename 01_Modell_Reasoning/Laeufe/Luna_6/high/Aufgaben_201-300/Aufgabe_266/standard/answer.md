Implemented `ImportItem.find_staged_or_pending` with default sources `amazon` and `idb`, and routed ISBN resolution through the local lookup. Added coverage for staged and pending matches, custom sources, and excluded statuses.

Verification: `pytest -q openlibrary/tests/core/test_imports.py` — 7 passed.