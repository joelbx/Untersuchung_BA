# Amazon language metadata fix

- Located `serialize(product)` and `clean_amazon_metadata_for_load(metadata)` in `openlibrary/core/vendors.py`.
- Located relevant existing tests in `openlibrary/tests/core/test_vendors.py`.
- Implemented ordered, exact-value deduplication of Amazon language display values; entries marked `Original Language` are excluded, and empty results omit the field.
- Added `languages` to the metadata accepted by `clean_amazon_metadata_for_load`.
- Added regression coverage for duplicate, missing, empty, and original-language-only values, plus cleaning assertions.
- Validation: `pytest -q openlibrary/tests/core/test_vendors.py` (37 passed), `ruff check` (passed), and `git diff --check` (passed). `black` is unavailable in the environment; no packages were downloaded.
