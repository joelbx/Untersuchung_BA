Implemented the IA metadata normalization. `get_ia_record` now separates ISBN-10/ISBN-13 values and publisher names/places, omitting empty normalized fields. The public helpers are in [utils.py](/app/openlibrary/plugins/upstream/utils.py:58); the importer is updated in [code.py](/app/openlibrary/plugins/importapi/code.py:337).

Updated existing import expectations in [test_code.py](/app/openlibrary/plugins/importapi/tests/test_code.py:38).

Verification: 17 relevant tests passed, and `git diff --check` passed.