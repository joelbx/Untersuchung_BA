# Checkpoint

Task: implement non-persistent preview support for catalog imports, plus observable cover URL validation, author matching/normalization, and normalized edition construction.

Implemented:
- Added `save` handling to `load`, `load_data`, `new_work`, and `load_author_import_records`; preview keys use UUID based `/books/__new__…`, `/works/__new__…`, and `/authors/__new__…` prefixes.
- Preview imports skip `save_many`, cover uploads, and Archive.org metadata writeback, and return `preview: true`, proposed `edits`, and `cover_accepted`.
- Added case insensitive hostname allowlist validation and applied it to both new and matched edition cover paths.
- Added `author_import_record_to_author` and `import_record_to_edition`, keeping old names as compatibility aliases. Author resolution handles normalized names, redirects, remote IDs/conflicts, year matching, and modified author records.
- Passed preview state through the general and Archive.org import endpoints.

Verification:
- Import API tests: 64 passed.
- Catalog import tests: 121 passed, 1 failed. The remaining legacy `test_covers_are_added_to_edition` expects a cover upload from `www.covers.org`, which is not in the configured allowlist and is correctly rejected under this issue's validation requirement.
- `ruff check` passed; Python compilation and `git diff --check` passed.

Constraints followed: only checked-out repository code and existing tests were used; no history, index baseline, or harness configuration was changed.
