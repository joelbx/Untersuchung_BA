Updated [vendors.py](/app/openlibrary/core/vendors.py) to include edition language names in Amazon imports, excluding “Original Language” entries, removing duplicates, and omitting an empty `languages` field. The metadata cleanup function now preserves `languages`.

Verification: all 36 vendor tests passed, and `git diff --check` passed.