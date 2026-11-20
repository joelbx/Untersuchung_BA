Updated [vendors.py](/app/openlibrary/core/vendors.py): Amazon language display names are preserved in order, original-language entries and duplicates are excluded, and `languages` is omitted when empty. The metadata cleaner now accepts the field.

Verification: `python -m pytest openlibrary/tests/core/test_vendors.py -q` — 33 passed. Updated `.codex-role-output/checkpoint.md`.