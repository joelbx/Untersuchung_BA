Updated [parse.py](/app/openlibrary/catalog/marc/parse.py) to import linked MARC 880 alternate-script names for personal authors in fields 100, 700, and 720. Added `name_from_list`, kept primary author fields, and deduplicated alternate names. Updated the relevant fixtures and added XML coverage.

Verification: all 124 MARC tests passed; `git diff --check` passed.