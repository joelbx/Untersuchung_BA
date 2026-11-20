Task: Add module-level check-in date formatting and patron update request validation.
Changes: Added make_date_string(year, month, day) with zero-padded optional components; retained check_ins.make_date_string compatibility. Added patron_check_ins.is_valid requiring id and either year or data. Added focused tests for both interfaces.
Verification: python -m pytest openlibrary/plugins/upstream/tests/test_checkins.py -q (18 passed); git diff --check passed.
