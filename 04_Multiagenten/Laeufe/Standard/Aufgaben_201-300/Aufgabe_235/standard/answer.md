Updated [parse.py](/app/openlibrary/catalog/marc/parse.py) to normalize personal names and import deduplicated alternate-script names from linked MARC 880 fields for `100`, `700`, and `720` authors. Updated the affected fixtures and added tests for multiple linked names.

Verification: all 122 MARC tests passed; `git diff --check` passed.