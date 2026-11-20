Task: Fix promise item metadata augmentation for incomplete records using ISBN-10 or Amazon ASIN.
Status: Complete. Incomplete records now augment before import API validation and at load; batch stages ISBN-10 first, records gauges, and tolerates lookup errors. Placeholders are removed before evaluating incompleteness.
Verification: 109 relevant pytest cases passed; ruff check and git diff --check passed.
Delegation: None used; no proposals to adopt or decline.
