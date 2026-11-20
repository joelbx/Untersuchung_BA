# Checkpoint

Resolved work Solr IA prioritization: public editions take precedence for lending fields; lendinglibrary editions are treated as borrowable. IA identifiers remain paired with selected editions.

Coverage: mixed public, in-library, and multiple print-disabled editions; lendinglibrary-only fallback.

Verification: python -m pytest openlibrary/tests/solr/test_update_work.py -q — 57 passed, 3 warnings. git diff --check — passed.
