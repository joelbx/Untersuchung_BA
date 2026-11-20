Implemented author matching fixes in [load_book.py](/app/openlibrary/catalog/add_book/load_book.py) and year extraction in [helpers.py](/app/openlibrary/core/helpers.py). Matching now checks exact names, alternate names, then surname plus matching extracted years; literal asterisks cannot act as name wildcards. Honorific removal now accepts and returns strings, handles title-only names and normalized exceptions, and runs in `build_query`.

Updated existing expectations and the differing date format fixture in [test_load_book.py](/app/openlibrary/catalog/add_book/tests/test_load_book.py).

Verification: **37 relevant tests passed**; `git diff --check` passed.