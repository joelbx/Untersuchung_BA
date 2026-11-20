Implemented language-aware Wikipedia links, valid Wikidata statement value extraction, and structured profiles for Wikipedia, Wikidata, and each Google Scholar identifier. The author infobox now displays those profiles using the current locale.

Verification: `python -m pytest openlibrary/tests/core/test_wikidata.py -q` — 7 passed.