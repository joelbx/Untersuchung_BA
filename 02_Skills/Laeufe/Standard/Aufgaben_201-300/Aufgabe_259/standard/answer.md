Updated the work Solr builder to select a public IA edition for `lending_edition_s` when one exists and keep its IA identifier paired with it. It now treats `lendinglibrary` editions as borrowable. Tests cover the mixed-edition case, including all IA IDs, collection names, and multiple print-disabled edition IDs.

Verification: 57 tests passed in `test_update_work.py`; `git diff --check` passed.