Updated [parse.py](/app/openlibrary/catalog/marc/parse.py) to normalize names from fields 100, 700, and 720 and add deduplicated `alternate_names` from linked 880 fields. Added linkage tests and updated affected fixture expectations.

The MARC test suite passes: **124 tests**.