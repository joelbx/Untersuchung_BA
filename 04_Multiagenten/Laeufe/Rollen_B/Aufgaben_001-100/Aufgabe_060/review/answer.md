VERDICT: FIX

The patch has two correctness gaps:

- [build_query](/app/openlibrary/catalog/add_book/load_book.py:324) and [build_author_reply](/app/openlibrary/catalog/add_book/__init__.py:240) require an author name. A record supplied with only an Open Library key or remote IDs therefore fails in the book import path. Allow identifier-only matches through both steps.
- [find_entity](/app/openlibrary/catalog/add_book/load_book.py:209) can choose a lower-key author whose other remote ID conflicts with the import, even when a compatible candidate exists. Exclude conflicting candidates before ranking, and handle IDs that identify different existing authors explicitly.

Relevant existing tests passed: `pytest -q openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/catalog/add_book/tests/test_add_book.py` (122 passed) and `pytest -q openlibrary/tests/core/test_models.py openlibrary/plugins/upstream/tests/test_merge_authors.py` (40 passed). These cases remain uncovered. No `TEST_ENVIRONMENT_PROBLEM`; I made no project code changes.