Task: Correct multi-edition Internet Archive availability and metadata in work Solr documents.
Changes: Updated `openlibrary/solr/update_work.py` to select public editions before loanable editions, classify legacy lending-library items as borrowable, and keep the selected edition ID paired with its IA identifier. Updated existing and added multi-edition tests, including multiple print-disabled IDs.
Verification: `pytest -q openlibrary/tests/solr/test_update_work.py` passed (58 tests); `pytest -q openlibrary/tests/solr` passed (61 tests); `git diff --check` passed.
Status: Implementation and review complete. Repository edits are limited to the Solr work builder and its existing test file.
