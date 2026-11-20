# Checkpoint

Task: Expand the affiliate queue element to generic identifiers, preserve compatibility, and verify locally.

Initial search: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` instead.

Implementation: `PrioritizedIdentifier` now stores a generic identifier and import staging flag, compares/hashes by identifier, serializes its public fields, and retains `PrioritizedISBN` plus legacy constructor/attribute access. Queue deduplication and batch staging use the new model.

Verification notes:
- `python -m black --check scripts/affiliate_server.py scripts/tests/test_affiliate_server.py` could not run: `/usr/local/bin/python: No module named black`. Formatter status from Black is unknown; Ruff formatting is used instead.
- An initial expanded pytest run failed because the test fixture attempted to patch an absent `web.amazon_api` attribute. The fixture was corrected with `raising=False`; this was a test setup issue.
