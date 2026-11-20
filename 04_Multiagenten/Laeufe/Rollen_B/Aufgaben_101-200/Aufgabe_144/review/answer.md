VERDICT: ACCEPT

The applied refactor has no identified code defects. `expand_record()` preserves the record expansion behavior, and no tracked `build_marc` references remain.

Tests executed:

- `python -m pytest -q openlibrary/catalog/merge/tests/test_merge_marc.py openlibrary/catalog/add_book/tests/test_match.py` — 11 passed, 2 xfailed.
- `python -m pytest -q openlibrary/catalog/add_book/tests openlibrary/catalog/merge/tests` — 85 passed, 8 skipped, 2 xfailed.
- `git diff --check` — passed.

TEST_ENVIRONMENT_PROBLEM: none. The review is recorded in [checkpoint.md](/app/.codex-role-output/checkpoint.md).