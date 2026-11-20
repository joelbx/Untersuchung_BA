VERDICT: FIX
Review complete. Two code defects remain in the applied patch:
1. A key-only or remote_ids-only author reaches build_query(), which unconditionally reads author['name'] at openlibrary/catalog/add_book/load_book.py:324. build_author_reply() also reads a['name'] at openlibrary/catalog/add_book/__init__.py:240. Thus identifier-only imports fail despite import_author() supporting them.
2. find_entity() ranks remote-ID candidates by match count and numeric key at openlibrary/catalog/add_book/load_book.py:209-218 without filtering conflicting IDs. A lower-key candidate matching VIAF but holding a different Goodreads ID wins over a compatible higher-key candidate, then merge_remote_ids raises, so the valid match is missed. Rank only compatible candidates; define clear handling when different IDs identify distinct existing authors.
Existing local tests executed successfully:
- pytest -q openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/catalog/add_book/tests/test_add_book.py — 122 passed.
- pytest -q openlibrary/tests/core/test_models.py openlibrary/plugins/upstream/tests/test_merge_authors.py — 40 passed.
No TEST_ENVIRONMENT_PROBLEM. Project code unchanged by reviewer.
