Task: Add override-validation support to /import/api and add is_promise_item utility.
Status: Complete.
Changes: The endpoint parses override-validation=true, passes the boolean through load() to validate_record(), and bypasses the three specified checks while retaining required fields. Added case-insensitive is_promise_item utility and focused tests.
Verification: pytest -q openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/plugins/importapi/tests/test_code.py (62 passed).
