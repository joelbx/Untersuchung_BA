Implemented cover host validation in [add_book/__init__.py](/app/openlibrary/catalog/add_book/__init__.py:79). `process_cover_url` accepts HTTP and HTTPS URLs from allowed hosts case insensitively, and removes the `cover` key whether the URL is valid or not. Both new and matched edition imports now use it.

Updated the existing cover fixture to use `archive.org`.

Verification: **109 tests passed** across `test_add_book.py` and `test_load_book.py`.