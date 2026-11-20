# Checkpoint

Task: Fix Solr document generation for works with multiple Internet Archive editions so public/loanable/print-disabled availability and IA metadata are represented correctly.

Implementation: `SolrProcessor.add_ebook_info` now selects a public edition for `lending_edition_s` when one is available, with the previous lending library and in library selection retained as fallbacks. Existing aggregation continues to include all IA identifiers and collections and all print disabled edition ids.

Regression coverage: Updated the existing multi edition expectation and added a fixture with public, in library, and print disabled editions; it checks `has_fulltext`, `public_scan_b`, lending edition, print disabled id, IA membership, and collection aggregation.

Validation: `python -m pytest openlibrary/tests/solr/test_update_work.py -q` passed (57 tests). `git diff --check` passed.
