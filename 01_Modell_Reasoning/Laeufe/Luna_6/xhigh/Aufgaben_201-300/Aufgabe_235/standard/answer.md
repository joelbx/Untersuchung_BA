Implemented alternate-script author parsing in [parse.py](/app/openlibrary/catalog/marc/parse.py:227). The parser now normalizes author names, resolves linked 880 fields for 100, 700, and 720 entries, and adds deduplicated `alternate_names`. Organization and event parsing remains unchanged.

Updated the affected MARC output snapshots and the required checkpoint.

Verification: `python -m pytest openlibrary/catalog/marc/tests/test_parse.py -q` — **59 passed**. `git diff --check` passed.