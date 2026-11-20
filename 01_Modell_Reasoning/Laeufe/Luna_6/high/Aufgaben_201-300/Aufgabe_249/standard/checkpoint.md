# Checkpoint

Task: resolve structured, language-aware Wikidata external profiles and display them in the author infobox.

Initial inspection found `openlibrary/core/wikidata.py` and `openlibrary/templates/authors/infobox.html`. `rg` is unavailable, so used `find` and standard text tools.

Implemented language-aware Wikipedia lookup with English fallback, tolerant statement value extraction, structured Wikipedia/Wikidata/Google Scholar profile generation, and rendering of the profiles in the author infobox with matching styling and SVG icons.

Verification: `pytest -q openlibrary/tests/core/test_wikidata.py` passed (7 tests); `git diff --check` passed. The existing test module covers cache behavior, not the newly added profile methods.
