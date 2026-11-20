Updated promise-item imports so incomplete JSON records use a staged or pending item to fill empty metadata fields **before validation**. Lookup prefers ISBN-10, then a B-prefixed Amazon ASIN. Complete records skip augmentation, existing non-empty fields are preserved, and batch staging failures are logged without stopping other items. The batch script also records total and incomplete counts with gauges and removes placeholder publisher values.

Validation now accepts either a complete record or a record with a title, source records, and a strong identifier. Added regression tests for augmentation and identifier selection.

Verification: **30 tests passed**; Ruff and `git diff --check` passed.