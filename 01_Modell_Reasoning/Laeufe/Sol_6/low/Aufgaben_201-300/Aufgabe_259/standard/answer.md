Updated the Solr work builder to prefer a public IA edition for `lending_edition_s` and keep `lending_identifier_s` matched to that edition. Added a regression test covering public, loanable, and multiple print-disabled editions, including the availability flags and IA metadata.

All 57 tests in `test_update_work.py` pass.