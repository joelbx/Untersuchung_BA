Updated the Solr builder to select a public edition for `lending_edition_s` and keep `lending_identifier_s` paired with it. The regression tests also cover IA membership, collection union, multiple print-disabled editions, and lending fallback.

Verification: all 57 tests in `test_update_work.py` pass; `git diff --check` is clean.