Task: migrate openlibrary/catalog/get_ia.py from urllib to requests.
Status: implementation and focused verification complete.
Changes: requests.get with headers and kwargs, raise_for_status, request exception handling, UTF-8 default when no charset; response.content for MARC and XML, response.text for text; Range header and content cap; migrated dependent marc_subject callers. Tests use requests.Response fixtures and cover status handling, retry, Range, XML, binary, text, charset, and dependent callers.
Checks:
- `pytest -q openlibrary/tests/catalog/test_get_ia.py openlibrary/catalog/marc/tests/test_get_subjects.py && git diff --check`: 102 passed; 5 warnings (pre-existing Genshi deprecation and calls to deprecated legacy functions).
- `pytest -q`: exit 1; 10 failed, 605 passed, 35 skipped, 5 xfailed, 1 xpassed, 182 errors. Failures are in vendor/infogami/infogami/infobase/tests/test_client.py and test_infobase.py. Collection errors include Python 2 syntax in installed dateutil and scripts/2011/04/test_olcompress.py, missing splinter, missing auth.yaml; runtime errors include missing USER and unavailable psycopg2/database setup. These are outside the touched code, so full suite status remains uncertain.
- `pytest -q --reruns 0 --tb=line > /tmp/get_ia_full_pytest.log 2>&1; tail -n 80 /tmp/get_ia_full_pytest.log`: same 10 failed/182 errors; command's shell exit is from tail, so first pytest invocation above supplies exit status. Full list of failures in /tmp/get_ia_full_pytest.log for this environment.
Tooling: rg unavailable (`/bin/bash: rg: command not found`); used local grep/find instead.
FAILED vendor/infogami/infogami/infobase/tests/test_client.py::TestRecentChanges::test_query_by_data
FAILED vendor/infogami/infogami/infobase/tests/test_client.py::TestSeq::test_seq
FAILED vendor/infogami/infogami/infobase/tests/test_client.py::TestSanity::test_reindex
FAILED vendor/infogami/infogami/infobase/tests/test_client.py::TestAccount::test_register
FAILED vendor/infogami/infogami/infobase/tests/test_infobase.py::TestInfobase::test_nested_things
FAILED vendor/infogami/infogami/infobase/tests/test_infobase.py::TestInfobase::test_property_cache
FAILED vendor/infogami/infogami/infobase/tests/test_infobase.py::TestInfobase::test_save
FAILED vendor/infogami/infogami/infobase/tests/test_infobase.py::TestInfobase::test_things
FAILED vendor/infogami/infogami/infobase/tests/test_infobase.py::TestInfobase::test_versions
FAILED vendor/infogami/infogami/infobase/tests/test_infobase.py::TestInfobase::test_versions_by_bot
