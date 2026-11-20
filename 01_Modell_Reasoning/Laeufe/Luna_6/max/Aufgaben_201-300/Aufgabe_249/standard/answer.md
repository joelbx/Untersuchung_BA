Implemented structured external profiles for Wikidata entities and added them to the author infobox.

- Added localized Wikipedia sitelink lookup with English fallback, robust statement value extraction, and multiple Google Scholar profiles in [wikidata.py](/app/openlibrary/core/wikidata.py).
- Re-enabled author Wikidata lookup in [models.py](/app/openlibrary/core/models.py).
- Rendered profile links and icons in the author infobox, with styling and the three requested SVG assets.

Verification: 32 existing tests passed; the infobox template parsed successfully; `git diff --check` was clean.