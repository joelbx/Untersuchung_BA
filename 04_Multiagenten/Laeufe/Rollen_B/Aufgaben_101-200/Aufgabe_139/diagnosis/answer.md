I traced the issue but did not edit project source or tests; this task was scoped to fault localization.

The likely fix spans four paths:

- [import_edition_builder.py](/app/openlibrary/plugins/importapi/import_edition_builder.py:111) validates during construction, before [code.py](/app/openlibrary/plugins/importapi/code.py:101) can pass the record to `add_book.load`. Augmentation must happen before that validation.
- [import_validator.py](/app/openlibrary/plugins/importapi/import_validator.py:16) requires authors, publishers, and a publish date. It has no strong-identifier alternative.
- [add_book/__init__.py](/app/openlibrary/catalog/add_book/__init__.py:990) looks up staged metadata only for a B-prefixed ASIN, even for complete records, and backfills only five fields. It needs the incomplete-record gate, ISBN-10 preference, and the additional eligible fields. Its normalization already removes `["????"]` publishers.
- [promise_batch_imports.py](/app/scripts/promise_batch_imports.py:92) stages only B-prefixed ASINs, regardless of completeness, and records no gauges. [stats.py](/app/openlibrary/core/stats.py:39) currently has no `gauge` function.

The fix should cover missing or empty title, authors, or publish date; preserve non-empty values; prefer ISBN-10 over a B-prefixed ASIN; and let lookup failures leave other items processing. Existing tests cover validation and placeholder removal, but I found no tests for promise-item augmentation or staging, so the full behavior remains unverified.