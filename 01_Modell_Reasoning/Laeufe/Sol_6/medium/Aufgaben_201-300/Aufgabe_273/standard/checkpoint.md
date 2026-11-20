Task: Fix make_work for documents missing author fields.
Status: Complete. Updated make_work to tolerate missing author fields, retain supplied cover URL, and keep metadata defaults. Annotated make_work and nested make_author. Added regression tests.
Verification: pytest -q openlibrary/plugins/upstream/tests/test_addbook.py (15 passed); git diff --check passed.
