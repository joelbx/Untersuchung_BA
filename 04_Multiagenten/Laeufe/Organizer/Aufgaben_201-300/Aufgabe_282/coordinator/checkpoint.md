Task: Add content.javascript.log_message.excludes and update JavaScript UI filtering.
Status: Implemented and verified.
Changes: Renamed old UI-level setting to content.javascript.log_message.levels with migration; added excludes dictionary; added _js_log_to_ui and fallback logger routing; regenerated settings documentation; added focused tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/config/test_configdata.py tests/unit/config/test_configfiles.py::TestYamlMigrations (106 passed, 1 rerun); git diff --check passed.
Note: Broader configfiles run found pre-existing Python 3.11 test_nul_bytes mismatch (expects ValueError, gets SyntaxError). No delegation used.
