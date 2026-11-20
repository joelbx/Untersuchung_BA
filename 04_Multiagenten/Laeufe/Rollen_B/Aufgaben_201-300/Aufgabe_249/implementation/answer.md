Implemented structured external profiles for Wikidata authors. `WikidataEntity` now resolves Wikipedia links by language with English fallback, extracts valid statement values, and returns Wikidata and Google Scholar profiles. The author infobox displays them with new SVG icons.

Verification: all 10 Wikidata tests pass; Ruff and `git diff --check` pass.