Implemented promise-item metadata augmentation, validation, batch staging, gauges, and placeholder publisher normalization.

Relevant changes are in [code.py](/app/openlibrary/plugins/importapi/code.py), [import_validator.py](/app/openlibrary/plugins/importapi/import_validator.py), [promise_batch_imports.py](/app/scripts/promise_batch_imports.py), [stats.py](/app/openlibrary/core/stats.py), and [import_edition_builder.py](/app/openlibrary/plugins/importapi/import_edition_builder.py).

Verification: 23 relevant tests passed, and `git diff --check` passed.