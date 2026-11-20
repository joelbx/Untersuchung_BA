Task: Fix make_work for documents missing author information.
Status: Complete. Updated make_work annotations, author handling, and optional metadata defaults; annotated nested make_author. Added regression tests for missing author fields and preserved metadata.
Verification: python -m pytest openlibrary/plugins/upstream/tests/test_addbook.py -q (15 passed); git diff --check passed.
