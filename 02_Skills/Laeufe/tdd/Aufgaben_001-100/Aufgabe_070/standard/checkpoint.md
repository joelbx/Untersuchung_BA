# Checkpoint

Task: normalize ISO-639-1 codes and English/native names in `format_languages`, then deduplicate canonical keys in first-occurrence order.

Implemented: ISO two-letter identifiers resolve from current language record metadata, with existing MARC lookup as fallback; names use the existing translated-name resolver against the current site's records; canonical keys are validated and deduplicated in input order.

TDD: regression cases failed first for German, Spanish, duplicate `eng`, missing `nb`, and mis-mapped `ga`. Initial whole-suite run showed five language test failures from the global language cache; fixed by resolving against current site records. `pytest -q openlibrary --reruns 0` passed: 2270 passed, 9 skipped, 8 xfailed. `ruff check openlibrary/catalog/utils/__init__.py openlibrary/tests/catalog/test_utils.py` passed with an existing pyproject deprecation warning. `git diff --check` passed.

Full suite check: `pytest -q --reruns 0` exited 1: 2389 passed, 21 skipped, 8 xfailed, 77 errors. No failing test assertions remain. The errors are setup/collection issues involving offline scripts/Infogami: `scripts/tests/test_isbndb.py` attempts an HTTPS request and gets ProxyError; the vendor Infogami duplicate plugin path raises ValueError; some tests require USER environment variable or unavailable PostgreSQL host `postgres`. The 77 error reports are listed below by name, including repeat setup errors:

- `ERROR scripts/tests/test_isbndb.py - requests.exceptions.ProxyError: HTTPSCon...`
- `ERROR vendor/infogami/infogami - ValueError: Plugin already registered under ...`
- `ERROR vendor/infogami/tests/test_infogami/test_account.py - KeyError: 'USER'`
- `ERROR vendor/infogami/tests/test_infogami/test_pages.py - KeyError: 'USER'`
- `ERROR infogami/infobase/tests/test_account.py::TestAccount::test_register - A...`
- `ERROR infogami/infobase/tests/test_account.py::TestAccount::test_register_failures`
- `ERROR infogami/infobase/tests/test_account.py::TestAccount::test_register_failures2`
- `ERROR infogami/infobase/tests/test_account.py::TestAccount::test_login_account`
- `ERROR infogami/infobase/tests/test_account.py::TestAccount::test_update - Ass...`
- `ERROR infogami/infobase/tests/test_client.py::TestRecentChanges::test_all - A...`
- `ERROR infogami/infobase/tests/test_client.py::TestRecentChanges::test_key - A...`
- `ERROR infogami/infobase/tests/test_client.py::TestRecentChanges::test_query_by_data`
- `ERROR infogami/infobase/tests/test_client.py::TestStore::test_getitem - Asser...`
- `ERROR infogami/infobase/tests/test_client.py::TestStore::test_contains - Asse...`
- `ERROR infogami/infobase/tests/test_client.py::TestStore::test_keys - Assertio...`
- `ERROR infogami/infobase/tests/test_client.py::TestStore::test_keys_unlimited`
- `ERROR infogami/infobase/tests/test_client.py::TestStore::test_key_value_items`
- `ERROR infogami/infobase/tests/test_client.py::TestStore::test_update - Assert...`
- `ERROR infogami/infobase/tests/test_client.py::TestSeq::test_seq - AssertionError`
- `ERROR infogami/infobase/tests/test_client.py::TestSanity::test_reindex - Asse...`
- `ERROR infogami/infobase/tests/test_client.py::TestAccount::test_register - As...`
- `ERROR infogami/infobase/tests/test_infobase.py::TestInfobase::test_nested_things`
- `ERROR infogami/infobase/tests/test_infobase.py::TestInfobase::test_property_cache`
- `ERROR infogami/infobase/tests/test_infobase.py::TestInfobase::test_save - Ass...`
- `ERROR infogami/infobase/tests/test_infobase.py::TestInfobase::test_things - A...`
- `ERROR infogami/infobase/tests/test_infobase.py::TestInfobase::test_versions`
- `ERROR infogami/infobase/tests/test_infobase.py::TestInfobase::test_versions_by_bot`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_all - Ass...`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_author - ...`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_ip - Asse...`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_bot - Ass...`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_key - Ass...`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_data - As...`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_query_by_data`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_kind - As...`
- `ERROR infogami/infobase/tests/test_read.py::TestRecentChanges::test_query_by_date`
- `ERROR infogami/infobase/tests/test_save.py::Test_get_records_for_save::test_new`
- `ERROR infogami/infobase/tests/test_save.py::Test_get_records_for_save::test_existing`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_save - AssertionE...`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_type_change - Ass...`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_with_author - Ass...`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_versions - Assert...`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_save_with_cross_refs`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_save_with_new_type`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_save_with_all_datatypes`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_save_with_long_string`
- `ERROR infogami/infobase/tests/test_save.py::Test_save::test_transaction - Ass...`
- `ERROR infogami/infobase/tests/test_save.py::TestIndex::test_monkeypatch - Ass...`
- `ERROR infogami/infobase/tests/test_save.py::TestIndex::test_compute_index - A...`
- `ERROR infogami/infobase/tests/test_save.py::TestIndex::test_dict_difference`
- `ERROR infogami/infobase/tests/test_save.py::TestIndex::test_diff_index - Asse...`
- `ERROR infogami/infobase/tests/test_save.py::TestIndex::test_diff_records - As...`
- `ERROR infogami/infobase/tests/test_save.py::TestIndex::test_compile_index - A...`
- `ERROR infogami/infobase/tests/test_save.py::TestIndex::test_too_long - Assert...`
- `ERROR infogami/infobase/tests/test_save.py::TestIndexWithDB::test_reindex - A...`
- `ERROR infogami/infobase/tests/test_save.py::TestPropertyManager::test_get_property_id`
- `ERROR infogami/infobase/tests/test_save.py::TestPropertyManager::test_rollback`
- `ERROR infogami/infobase/tests/test_save.py::TestPropertyManager::test_copy - ...`
- `ERROR infogami/infobase/tests/test_seq.py::TestSeq::test_seq - AssertionError`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_insert - Asserti...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_update - Asserti...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_conflicts - Asse...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_notfound - Asser...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_delete - Asserti...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_query - Assertio...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_query_order - As...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_query_include_docs`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_indexer - Assert...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_indexer2 - Asser...`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_typewise_indexer`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_typewise_indexer2`
- `ERROR infogami/infobase/tests/test_store.py::TestStore::test_multiput - Asser...`
- `ERROR infogami/infobase/tests/test_writequery.py::TestSaveProcessor::test_errors`
- `ERROR infogami/infobase/tests/test_writequery.py::TestSaveProcessor::test_process_value`
- `ERROR vendor/infogami/test/test_dbstore.py::TestSaveTest::testSave - psycopg2...`
- `ERROR vendor/infogami/test/test_dbstore.py::TestSaveTest::test_type - psycopg...`
- `ERROR vendor/infogami/test/test_dbstore.py::TestSaveTest::test_expected_type`

Tooling: `rg -n "def format_languages|format_languages|class InvalidLanguage" . --glob '!*.lock'` could not run because `rg` is not installed (`/bin/bash: rg: command not found`); used local grep/find instead.
Final targeted rerun after docstring update: `pytest -q openlibrary/tests/catalog/test_utils.py --reruns 0` passed (100 tests, 3 dependency deprecation warnings).
