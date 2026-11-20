Task: Fix multi-edition IA availability prioritization and metadata in Solr work documents.
Status: Implemented public-first edition selection; paired lending edition and identifier; classify lendinglibrary as borrowable; preserved print-disabled and collection aggregation. Updated existing test and added mixed-edition and lendinglibrary coverage.
Verification: pytest -q openlibrary/tests/solr/test_update_work.py (58 passed); git diff --check passed.
Delegation: None; solved directly.
