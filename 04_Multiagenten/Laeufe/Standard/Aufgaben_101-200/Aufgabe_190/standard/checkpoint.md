Task: nonpersistent import preview, cover validation, author/edition normalization.
Status: implemented in add_book and importapi; targeted tests pass (131). New tests cover new and matched preview and cover host acceptance. Existing cover test updated for allowlist behavior.
Validation: pytest -q openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/plugins/importapi/tests/test_code.py (131 passed); ruff check on changed implementation files passes; git diff --check passes.
Constraints: local repository and tests only; no git history/index/harness changes.
