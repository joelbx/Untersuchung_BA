Updated the Solr work builder to prioritize a public IA edition for `lending_edition_s` and keep `lending_identifier_s` matched to that edition. It also classifies `lendinglibrary` editions as borrowable. The mixed-edition test now checks fulltext, public-scan, IA collection, and multiple print-disabled metadata.

Verification: all 57 tests in `openlibrary/tests/solr/test_update_work.py` pass.