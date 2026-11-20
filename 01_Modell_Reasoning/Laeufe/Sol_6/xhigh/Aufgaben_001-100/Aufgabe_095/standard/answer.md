Added the module-level `make_date_string` function and `patron_check_ins.is_valid` in [checkins.py](/app/openlibrary/plugins/upstream/checkins.py). Existing check-in callers still work.

The existing check-in tests pass (5/5), and direct checks of the new interfaces pass. This checkout has no patron update route, so the validator is available but is not yet called by a request handler.