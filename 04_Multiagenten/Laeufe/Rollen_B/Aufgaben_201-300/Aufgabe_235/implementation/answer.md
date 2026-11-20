Implemented alternate-script author imports in [parse.py](/app/openlibrary/catalog/marc/parse.py). Personal authors from 100 and promoted 700/720 fields now use normalized names and collect deduplicated names from linked 880 fields. I added linkage tests and updated affected binary expectations.

The MARC test suite passes: **122 tests**.