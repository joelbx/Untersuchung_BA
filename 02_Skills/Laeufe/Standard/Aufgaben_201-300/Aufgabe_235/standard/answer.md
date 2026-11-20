Updated [parse.py](/app/openlibrary/catalog/marc/parse.py) to normalize personal names and dates and import linked 880 names into `alternate_names` for author entries from 100, 700, and 720 fields. Added focused tests and updated the affected MARC fixtures.

Verification: `git diff --check` and all 124 MARC tests passed.