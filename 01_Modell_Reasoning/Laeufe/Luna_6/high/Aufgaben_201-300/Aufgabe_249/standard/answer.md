Implemented structured Wikidata profiles and displayed them in the author infobox. Wikipedia links use the requested language with English fallback; Google Scholar entries are generated for each valid P1960 identifier.

Verification: `pytest -q openlibrary/tests/core/test_wikidata.py` passed (7 tests), and `git diff --check` passed. The existing test module does not cover the new profile methods.