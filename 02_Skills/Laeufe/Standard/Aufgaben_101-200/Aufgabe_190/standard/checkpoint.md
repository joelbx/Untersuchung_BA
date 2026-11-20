# Import preview implementation checkpoint

Status: implemented preview imports for new and matched editions, temporary author/work/edition keys, cover host validation, normalized conversion entry points, and endpoint parameters. Added preview tests and updated the cover test to use an allowed host.

Tooling note: `rg` is unavailable (`/bin/bash: line 1: rg: command not found`); used `find` and `grep`. No download was needed.

Checks: `pytest -q openlibrary/catalog/add_book/tests openlibrary/plugins/importapi/tests/test_code.py` passed (165 tests). `git diff --check` passed.
