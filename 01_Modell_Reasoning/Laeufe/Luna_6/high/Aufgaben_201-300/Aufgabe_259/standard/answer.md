Updated Solr edition prioritization so a public edition is selected for `lending_edition_s` when available, while retaining lending library and in library editions as fallbacks. Added regression coverage for a work with public, loanable, and print disabled editions, including its availability flags and IA metadata.

Validation: `57` tests passed in `openlibrary/tests/solr/test_update_work.py`; `git diff --check` passed.

Changed [update_work.py](/app/openlibrary/solr/update_work.py) and [test_update_work.py](/app/openlibrary/tests/solr/test_update_work.py).