VERDICT: ACCEPT
Reviewed the applied diff in openlibrary/solr/update_work.py and openlibrary/tests/solr/test_update_work.py. The public edition is selected ahead of lendinglibrary and inlibrary editions, with its matching OCAID. Existing build_data coverage confirms has_fulltext, public_scan_b, IA membership, collection union, and print-disabled edition IDs. No code defect found.
Tests: `pytest -q openlibrary/tests/solr/test_update_work.py` — 57 passed. `pytest -q openlibrary/tests/solr` — 60 passed. `git diff --check` — passed. No TEST_ENVIRONMENT_PROBLEM; only deprecation warnings.
