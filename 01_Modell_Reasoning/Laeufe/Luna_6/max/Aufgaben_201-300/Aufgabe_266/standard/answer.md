Added `STAGED_SOURCES` and `ImportItem.find_staged_or_pending` to build `{source}:{identifier}` IDs and return matching staged or pending rows. `Edition.from_isbn` now uses the helper.

Verification: `python -m pytest openlibrary/tests/core/test_imports.py` — 5 passed; `git diff --check` clean.

Updated [checkpoint.md](/app/.codex-role-output/checkpoint.md). Changes are in [imports.py](/app/openlibrary/core/imports.py:21) and [models.py](/app/openlibrary/core/models.py:409).