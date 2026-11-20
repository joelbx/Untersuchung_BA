Resolved the promise-item import issue. Incomplete records now use ISBN-10 first, then a B-prefixed Amazon ASIN, to fill missing staged metadata before API validation. Existing non-empty fields are preserved, and placeholder values are removed before completeness is checked. Validation accepts either a complete record or one with a title, source records, and a strong identifier.

The [batch importer](/app/scripts/promise_batch_imports.py:99) stages only incomplete records, logs lookup failures and continues, and records total and incomplete gauges. I delegated the batch and validation changes plus a read-only review, then integrated and verified the patch.

**Verification:** 149 relevant tests passed; Ruff and `git diff --check` passed.