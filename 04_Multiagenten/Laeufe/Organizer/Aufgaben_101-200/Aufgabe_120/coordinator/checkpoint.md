Task: coverstore zip archival and verified finalization.
Status: implemented and tested. See modified archive.py, code.py, schema.py/sql, README.md and new test_archive.py.
Test evidence: python -m pytest openlibrary/coverstore/tests -q: 20 passed, 7 skipped. compileall and git diff --check passed.
Delegation: none; solved directly.
