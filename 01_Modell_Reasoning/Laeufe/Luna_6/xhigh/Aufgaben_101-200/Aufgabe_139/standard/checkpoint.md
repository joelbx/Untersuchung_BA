# Checkpoint

Task: resolve promise-item metadata augmentation for incomplete import records.

Completed:
- Import parsing now augments incomplete records before builder validation, preferring ISBN-10 and then B* ASIN.
- Staged/pending metadata fills missing or placeholder fields in place; lookup errors are logged and ignored.
- Validation accepts either complete metadata or a title/source record with a strong identifier.
- Promise batch lookup stages only incomplete records, supports ISBN-10 lookups, and emits total/incomplete gauges.
- Existing add-book augmentation is also limited to incomplete records. Publisher placeholder normalization was already present.

Verification: 110 focused existing tests passed; Ruff and `git diff --check` passed.
