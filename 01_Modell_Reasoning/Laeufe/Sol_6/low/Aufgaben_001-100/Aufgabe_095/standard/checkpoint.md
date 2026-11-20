Task: add module-level check-in date formatting and patron update validation.
Inspected: openlibrary/plugins/upstream/checkins.py; existing formatter is an instance method.
Result: added module-level formatter, kept instance compatibility, and added patron_check_ins.is_valid. Added focused tests. `pytest -q openlibrary/plugins/upstream/tests/test_checkins.py`: 7 passed. `git diff --check`: clean.
