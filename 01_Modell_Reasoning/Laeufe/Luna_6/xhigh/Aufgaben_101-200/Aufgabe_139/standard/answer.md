Implemented incomplete-record augmentation before import validation. ISBN-10 is preferred; otherwise, records can use a B* ASIN. Staged metadata fills empty fields in place, and lookup failures are logged without stopping processing.

Validation now accepts complete records or records with a title, source record, and strong identifier. The promise batch script stages only incomplete records and emits total and incomplete record gauges. Existing publisher placeholder normalization remains in place.

Verification: **110 focused tests passed**, Ruff passed, and `git diff --check` passed.