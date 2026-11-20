Implemented the import augmentation flow. Incomplete records now look up staged or pending metadata before validation, preferring ISBN-10 and then a B* ASIN. Validation accepts either a complete book record or a title, source record, and strong identifier. Promise batches stage only incomplete records and emit total and incomplete gauges.

The existing normalization already removes the `["????"]` publisher placeholder. Lookup failures are logged without interrupting batch processing.

**Verification:** 103 focused tests passed; `git diff --check` passed.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)