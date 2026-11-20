# Progress

- Located `WikidataEntity` in `openlibrary/core/wikidata.py`.
- Added language-aware Wikipedia lookup, statement extraction, and structured external profiles to `WikidataEntity`.
- Rendered profile icons in the author infobox and added the three referenced SVG assets.
- Added focused coverage for localized and fallback Wikipedia links, malformed statements, and multiple Google Scholar identifiers.
- Checks passed: `python -m pytest openlibrary/tests/core/test_wikidata.py -q` (14 passed), `ruff check openlibrary/core/wikidata.py openlibrary/tests/core/test_wikidata.py`, and `git diff --check`.
