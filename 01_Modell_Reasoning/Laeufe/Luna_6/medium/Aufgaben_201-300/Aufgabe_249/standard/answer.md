Implemented structured Wikidata profiles in [wikidata.py](/app/openlibrary/core/wikidata.py), including language-aware Wikipedia fallback, resilient statement value extraction, Wikidata links, and one Google Scholar link per P1960 identifier.

The author infobox now displays those profiles, and I removed an early `return None` that prevented `Author.wikidata()` from fetching entities.

Verification: `pytest -q openlibrary/tests/core/test_wikidata.py` passed (7 tests); `git diff --check` passed.