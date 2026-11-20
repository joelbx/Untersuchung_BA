Updated `get_ia_record` to split IA ISBNs into `isbn_10` and `isbn_13`, and publisher entries into `publishers` and `publish_places`. The public utilities are in [utils.py](/app/openlibrary/plugins/upstream/utils.py); empty or unusable values are omitted.

Updated the importer and utility tests. **All 33 focused tests passed**, and `git diff --check` found no whitespace errors.