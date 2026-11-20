Implemented structured Wikidata profiles on the author infobox. `WikidataEntity` now resolves Wikipedia links by requested language with English fallback, extracts valid statement values, and returns Wikidata plus one Google Scholar link per P1960 identifier. I also fixed `Author.wikidata()` so the infobox can reach the entity data.

The infobox, styles, and three SVG icons were handled by one delegated agent; another added focused tests. The combined patch passed **48 tests**, Ruff, stylelint, template and SVG parsing, and `git diff --check`.

Profiles appear when the author’s Wikidata entity is available under the existing cache and fetch rules.