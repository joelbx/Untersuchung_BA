Updated the [Solr work builder](/app/openlibrary/solr/update_work.py) to prefer a public IA edition for `lending_edition_s` and keep its IA identifier paired with it. The multi-edition test now covers the availability flags, IA IDs, collection union, and multiple print-disabled edition IDs.

Validation: **57 relevant tests passed**; `git diff --check` passed.