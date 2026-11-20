Updated [vendors.py](/app/openlibrary/core/vendors.py:259) to extract Amazon language display values, exclude “Original Language,” deduplicate them, and omit `languages` when empty. The metadata cleaner now preserves the field.

Validation: `pytest -q openlibrary/tests/core/test_vendors.py` — 33 passed. `git diff --check` passed.