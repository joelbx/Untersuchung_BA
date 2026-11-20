Added the module-level `make_date_string` formatter and `patron_check_ins.is_valid` in [checkins.py](/app/openlibrary/plugins/upstream/checkins.py). The update handler now rejects requests missing an event ID or updatable content, checks event ownership, and stores normalized dates. I also fixed the data update method so the handler can call it.

The relevant tests pass: **27 passed**.