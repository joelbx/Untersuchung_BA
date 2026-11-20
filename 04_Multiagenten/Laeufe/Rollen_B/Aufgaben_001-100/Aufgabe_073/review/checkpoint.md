VERDICT: ACCEPT
Reviewed openlibrary/core/vendors.py and openlibrary/tests/core/test_vendors.py. Language extraction preserves Amazon display names, excludes Type == "Original Language", removes duplicates while retaining order, and omits the key when no values remain. Metadata cleaning accepts languages.
Tests: `python -m pytest openlibrary/tests/core/test_vendors.py -q` — 36 passed (3 deprecation warnings). `git diff --check` — passed. No code defects or test environment problems found.
