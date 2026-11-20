Task: Replace urllib HTTP usage in openlibrary/catalog/get_ia.py with requests.
Status: Complete. Migrated GET/retry/status/encoding behavior and all response consumers; updated deprecated MARC subject callers. Added focused tests.
Validation: pytest -q openlibrary/tests/catalog/test_get_ia.py openlibrary/catalog/marc/tests/test_get_subjects.py (95 passed); git diff --check passed.
Constraints respected: local repository only; no git history/index or harness changes.
