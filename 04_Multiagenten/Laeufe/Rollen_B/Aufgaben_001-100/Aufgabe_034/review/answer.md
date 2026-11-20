VERDICT: ACCEPT

The applied patch separates IA ISBNs into `isbn_10` and `isbn_13`, splits publisher names from publication places, and preserves the other `get_ia_record` fields. I found no correctness or regression issue.

Tests executed:

- `python -m pytest openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py -q` — 29 passed.
- `python -m pytest openlibrary/plugins/importapi/tests -q` — 17 passed.
- `git diff --check` — passed.

Pytest reported two dependency warnings in each run; no tests failed.