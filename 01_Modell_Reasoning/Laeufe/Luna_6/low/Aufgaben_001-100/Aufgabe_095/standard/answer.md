Implemented module-level `make_date_string` with zero padding and partial-date handling, and added `patron_check_ins.is_valid` to require an event ID and either a year or data payload. The existing handler keeps its method wrapper for compatibility.

Validation: `pytest -q openlibrary/plugins/upstream/tests/test_checkins.py` — 5 passed.