Updated [parse.py](/app/openlibrary/catalog/marc/parse.py) to normalize names for 100, 700, and 720 author entries and add deduplicated `alternate_names` from linked 880 fields. Updated the expected MARC results and added linkage tests.

Verification: all 124 MARC tests pass; `git diff --check` passes.