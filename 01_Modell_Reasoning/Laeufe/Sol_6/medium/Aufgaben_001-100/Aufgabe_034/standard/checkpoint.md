Task: Normalize Internet Archive ISBN and publisher metadata in get_ia_record.
Status: Implemented and verified.
Changes: Added public ISBN and publisher splitting utilities; importer emits isbn_10/isbn_13 and publishers/publish_places; updated existing expectations and added mixed, string, and empty input coverage.
Verification: pytest on importapi/test_code.py and upstream/test_utils.py passed; git diff --check passed.
