Implemented incomplete promise-item metadata augmentation. Parsing now looks up staged metadata by ISBN-10 first, then B* ASIN, fills only empty fields, and validates after augmentation. Validation also accepts records with a strong identifier, and placeholder metadata is normalized before completeness checks.

Batch imports now stage only incomplete records, log lookup failures per item, and report total and incomplete record gauges when statsd is available.

Relevant existing suites passed: **108 passed**. `git diff --check` is clean.

Key files: [import API](</app/openlibrary/plugins/importapi/code.py:120>), [validator](</app/openlibrary/plugins/importapi/import_validator.py:24>), [promise batch script](</app/scripts/promise_batch_imports.py:149>), [stats](</app/openlibrary/core/stats.py:59>).