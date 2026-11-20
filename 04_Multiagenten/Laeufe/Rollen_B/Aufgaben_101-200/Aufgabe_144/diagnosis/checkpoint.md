# Fault localization checkpoint

`build_marc` is defined only in `openlibrary/catalog/merge/merge_marc.py` and delegates title expansion to that module's `build_titles`. It combines `isbn`, `isbn_10`, and `isbn_13`; copies six comparison fields; and filters only `publish_country` sentinel values. Direct callers are `add_book/__init__.py`, `add_book/match.py`, and two existing test modules. `compare_authors` and matching comments/docstrings still name `build_marc`.

Likely change surface: move expansion (and its title helper or equivalent import) to `catalog/utils/__init__.py`, update imports/calls/docs/tests, and remove `merge_marc.build_marc`. Preserve title variants and 25-character short title, ISBN aggregation, copied value types, and country filtering. `catalog/merge/merge.py` has a separate duplicate `build_titles`, which may matter for dependency placement. Requested return annotation is narrower than actual values (`number_of_pages` is an int; `authors` and `contribs` are lists of dicts).

Project source and tests have not been changed.
