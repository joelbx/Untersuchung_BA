Added module-level `make_date_string` with zero-padded partial dates and `patron_check_ins.is_valid` to require an event ID and updatable content in [checkins.py](/app/openlibrary/plugins/upstream/checkins.py). Existing `check_ins.make_date_string` calls still work.

The relevant test file passed: **7 tests**.