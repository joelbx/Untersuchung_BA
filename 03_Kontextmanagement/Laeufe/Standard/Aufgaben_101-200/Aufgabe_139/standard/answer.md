Updated promise-item imports so incomplete records use an available ISBN-10 first, then a B-prefixed ASIN, to fill missing fields from staged metadata before validation. The batch script now stages only incomplete records, records total and incomplete gauges, and continues after lookup failures.

Validation now accepts either a complete record or a title, source record, and strong identifier. Placeholder publishers are removed during normalization.

Verification: 36 relevant tests passed; targeted Ruff and `git diff --check` passed.