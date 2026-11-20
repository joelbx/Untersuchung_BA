# Checkpoint

Task: resolve incomplete promise-item metadata augmentation in `/app`.

Findings:
- `import_edition_builder` currently validates during construction, before `parse_data` can augment records.
- `add_book` currently supplements only B* ASIN records and does so after parsing.
- Promise batch staging only requests B* ASIN metadata, with no incomplete-record filter or gauges.
- Placeholder cleanup already exists in `add_book.normalize_import_record` for publishers, authors, and publish dates.
- Existing relevant suites are under `openlibrary/plugins/importapi/tests`, `openlibrary/catalog/add_book/tests`, and `scripts/tests/test_promise_batch_imports.py`.

Planned changes: defer builder validation until `get_dict`; augment incomplete parsed records by ISBN-10 first, then B* ASIN; allow strong-identifier validation; share placeholder cleanup/completeness checks with batch staging; add gauges; preserve per-item processing on lookup failures.

Progress:
- Import API parsing now normalizes placeholders, attempts staged metadata lookup for incomplete records using ISBN-10 first then a B* ASIN, and validates the enriched record.
- Validation accepts either the existing complete book model or a title/source-record record with ISBN-10, ISBN-13, or LCCN.
- Promise batch staging now filters complete records, prefers ISBN-10, logs per-item lookup failures, and reports total/incomplete gauges when statsd is configured.
- Placeholder cleanup is shared with the import path; the legacy `add_book` supplementer delegates to the import API helper.
- Relevant existing tests pass: 108 passed. The promise script suite required `PYTHONPATH=/app/scripts:/app` because its `_init_path` import is top-level.

No history, index baseline, or harness configuration changes.
