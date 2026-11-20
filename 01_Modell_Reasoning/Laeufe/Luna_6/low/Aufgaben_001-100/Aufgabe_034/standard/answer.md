Implemented IA metadata normalization:

- Added `get_isbn_10_and_13` and `get_publisher_and_place` in [utils.py](/app/openlibrary/plugins/upstream/utils.py).
- Updated `get_ia_record` to emit `isbn_10`, `isbn_13`, `publishers`, and `publish_places`, omitting empty fields and the old singular fields.
- Updated the existing import test expectations and wrote the required checkpoint.

The focused test run still reports **2 failures** in the language warning cases: the expected record includes `publishers`, while the actual result omits it. The other focused tests passed.