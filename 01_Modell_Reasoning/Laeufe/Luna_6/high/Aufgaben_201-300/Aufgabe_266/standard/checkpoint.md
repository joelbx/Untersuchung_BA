# Checkpoint

Issue: add a local query for staged or pending import records keyed by known source prefixes and identifiers.

Implemented `ImportItem.find_staged_or_pending` with default sources `amazon` and `idb`; routed ISBN resolution through the helper; added coverage for matching statuses and custom sources.

Verification: `pytest -q openlibrary/tests/core/test_imports.py` passed (7 tests).
