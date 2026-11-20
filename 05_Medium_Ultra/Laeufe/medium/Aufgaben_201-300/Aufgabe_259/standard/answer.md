Updated the Solr work builder to prefer a public IA edition for `lending_edition_s` and keep `lending_identifier_s` matched to it. The mixed-edition test now checks the availability flags, IA IDs, collection union, and multiple print-disabled edition IDs.

All 57 tests in `test_update_work.py` pass; `git diff --check` passes.