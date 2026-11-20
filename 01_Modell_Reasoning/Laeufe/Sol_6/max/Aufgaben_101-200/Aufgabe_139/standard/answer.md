Promise-item imports now backfill missing metadata from staged items using ISBN-10 first, then a B-prefixed ASIN. The import API enriches records before validation; complete records skip augmentation. Batch staging, strong-identifier validation, gauges, placeholder cleanup, and per-item failure logging are also updated.

**Verified:** 208 relevant tests passed; Ruff and `git diff --check` passed.