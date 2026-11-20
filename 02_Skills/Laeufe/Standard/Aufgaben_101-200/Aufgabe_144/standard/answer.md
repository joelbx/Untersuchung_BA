Moved edition expansion to `openlibrary.catalog.utils.expand_record`, updated the add book matching callers and documentation, and removed `build_marc` from `merge_marc.py`. Title expansion now lives in utils, with the existing `build_titles` import path preserved.

Validation: 85 tests passed, 8 skipped, 2 expected failures. Ruff and `git diff --check` passed.