Updated `get_ia_record` to emit separate `isbn_10`, `isbn_13`, `publishers`, and `publish_places` lists, omitting empty fields. The new public utilities in [utils.py](/app/openlibrary/plugins/upstream/utils.py) handle string and list inputs, extra whitespace, and invalid ISBN values.

Verification: all 29 targeted tests and all 17 import API tests passed. `ruff` was unavailable.