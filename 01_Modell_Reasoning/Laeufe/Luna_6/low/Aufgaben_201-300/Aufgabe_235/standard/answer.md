Implemented author parsing for MARC fields 100, 700, and 720, including normalized linked 880 names in `alternate_names`. Organization and event parsing remains unchanged.

The focused `read_author_person` test passes. The full `test_parse.py` run exposed a linkage bug during the initial implementation; I fixed the immediate error but did not rerun the full suite.