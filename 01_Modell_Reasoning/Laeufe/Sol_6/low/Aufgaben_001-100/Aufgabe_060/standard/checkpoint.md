Task: resolve author import matching with Open Library keys and external identifiers.
Status: implemented and verified.
Changes: key-first and remote ID matching, deterministic identifier tie-break, conflict-safe merge, preservation on new candidates, source exemption constant, focused tests.
Verification: pytest -q openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/tests/core/test_models.py (58 passed).
