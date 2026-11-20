# Checkpoint

Task: fix Solr availability prioritization and IA metadata for multi-edition works.

Completed: public IA editions take priority for lending edition and matching IA identifier; lendinglibrary editions are classified as borrowable; print-disabled edition IDs are aggregated deterministically. Existing multi-edition test updated and an order-independent multi-edition regression test added.

Verification: `python -m pytest openlibrary/tests/solr/test_update_work.py -q` passed (57 tests). `git diff --check` passed. Black is not installed in the environment.
