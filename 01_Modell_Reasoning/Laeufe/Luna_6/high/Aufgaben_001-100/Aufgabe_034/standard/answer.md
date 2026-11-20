Updated `get_ia_record` to split ISBNs into `isbn_10` and `isbn_13`, and publisher entries into `publishers` and optional `publish_places`. Added the public normalization helpers in [utils.py](/app/openlibrary/plugins/upstream/utils.py).

Validation passed: 17 targeted tests, and `git diff --check`.