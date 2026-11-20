# Checkpoint

Task: implement structured external profiles for Wikidata entities and show them on author infoboxes.

Initial state: git status was clean. `rg` was unavailable, so local inspection used `find` and `grep`.

Implemented:
- `WikidataEntity` now resolves Wikipedia sitelinks with English fallback, extracts valid statement content, and returns Wikipedia, Wikidata, and one Google Scholar profile per P1960 identifier.
- The author model now reaches the Wikidata lookup when a remote ID is present. The author infobox uses the existing cache-backed fetch for all viewers and renders the structured profiles, with local SVG icons and styling.
- Added model tests for language fallback, malformed statements, multiple identifiers, and author lookup.

Verification: 45 relevant pytest tests passed; Ruff, stylelint, LESS compilation, template compilation, SVG XML parsing, and `git diff --check` passed. Existing tool deprecation warnings were non-failing.
