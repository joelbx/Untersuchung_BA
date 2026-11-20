# Checkpoint

Task: add structured, language-aware external profile retrieval to `WikidataEntity` and display the profiles in author infoboxes.

Completed:
- Added Wikipedia sitelink selection for the requested language, regional locale fallback, and English fallback.
- Added robust statement `value.content` extraction and one Google Scholar profile for each valid P1960 identifier.
- Added Wikipedia and Wikidata built-in profiles, and rendered all profiles with icons in the author infobox.
- Re-enabled `Author.wikidata()` lookup so cached Wikidata data can reach author pages.
- Added the specified local SVG icon assets and infobox styling.

Verification:
- `pytest -q openlibrary/tests/core/test_wikidata.py openlibrary/tests/core/test_models.py`: 32 passed.
- Author infobox template parses successfully.
- `git diff --check`: clean.

Constraints observed: local repository code and existing tests only; no git history, index baseline, or harness configuration changes.
