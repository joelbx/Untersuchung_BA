# MARC alternate-script author import

Status: Complete.

Updated `read_author_person` to normalize author names and dates and collect distinct names from matching 880 linkages for 100, 700, and 720 fields. Added `name_from_list`, XML coverage for all three author tags, and updated two binary fixture expectations containing linked author names. Organization and event parsing is unchanged.

Verification: `pytest -q openlibrary/catalog/marc/tests --reruns 0` — 124 passed. `git diff --check` passed.
