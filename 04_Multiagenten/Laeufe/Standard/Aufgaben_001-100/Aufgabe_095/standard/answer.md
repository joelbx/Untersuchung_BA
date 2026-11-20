Added the module-level `make_date_string` function and `patron_check_ins.is_valid` in [checkins.py](/app/openlibrary/plugins/upstream/checkins.py). The formatter zero-pads dates at the supplied precision; validation requires an `id` and either `year` or `data`. Existing `check_ins.make_date_string` calls still work.

The check-in tests pass: **18 passed**.