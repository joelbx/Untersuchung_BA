# Coverstore archival work

Implemented uncompressed ZIP staging with zero-padded item, batch, and cover names; per-batch local locks; exact upload checks; and database `failed`/`uploaded` state. Upload waits until the serial ID range is closed. Finalization requires all four ZIPs locally and remotely, validates archive data and expected members, updates all filename fields to archive.org URLs, then removes staged ZIPs. Retrieval reads staged ZIPs and redirects uploaded records to their stored URLs. Legacy tar batches can be reconciled after verifying all four tar/index pairs remotely.

Verification: `python -m pytest openlibrary/coverstore/tests -q` passed (24 passed, 7 skipped). `ruff check` passed on touched Python files, and `git diff --check` passed.

Legacy tar content is not converted to ZIP in place; conversion requires access to its stored contents. Local file locks serialize jobs on one coverserver; separate hosts require a shared lock.
