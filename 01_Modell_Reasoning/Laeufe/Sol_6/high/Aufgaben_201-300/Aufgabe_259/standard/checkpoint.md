# Checkpoint

Resolved multi-edition IA availability in openlibrary/solr/update_work.py. Public editions now take priority for lending_edition_s and lending_identifier_s; lendinglibrary is treated as borrowable, and print-disabled edition IDs are joined deterministically. IA IDs and collection union remain aggregated across all IA editions. Expanded openlibrary/tests/solr/test_update_work.py for public edition priority, multiple print-disabled editions, IA aggregation, and matched lending identifiers. Verification: pytest -q openlibrary/tests/solr (61 passed); git diff --check passed.
