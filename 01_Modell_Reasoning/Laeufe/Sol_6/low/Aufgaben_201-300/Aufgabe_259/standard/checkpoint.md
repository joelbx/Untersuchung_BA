Task: Fix multi-edition IA availability selection and aggregation in Solr work documents.
Status: Implemented public edition priority with matching IA identifier; added regression coverage for public, loanable, and multiple print-disabled editions.
Verification: pytest -q openlibrary/tests/solr/test_update_work.py (57 passed); git diff --check passed.
