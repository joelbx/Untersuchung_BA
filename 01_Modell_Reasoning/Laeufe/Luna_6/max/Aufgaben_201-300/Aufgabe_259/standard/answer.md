Updated [update_work.py](/app/openlibrary/solr/update_work.py) so a public scan sets `public_scan_b` and its edition is selected for `lending_edition_s` ahead of lending-library or in-library editions. Existing lending fallbacks remain when no public scan exists. The IA identifiers, collection union, and print-disabled edition IDs continue to aggregate across editions.

Updated the mixed-edition regression case to expect the public edition, OL2M.

Verification: `python -m pytest openlibrary/tests/solr/test_update_work.py -q` — 56 passed. `git diff --check` passed.