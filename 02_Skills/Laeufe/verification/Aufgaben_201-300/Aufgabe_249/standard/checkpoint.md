# Checkpoint

Task: add structured external profiles to WikidataEntity and display them on the author infobox.

Implemented:
- Language-aware Wikipedia sitelink lookup with English fallback.
- Statement content extraction that skips malformed entries.
- Wikipedia, Wikidata, and multiple Google Scholar profile records.
- Author infobox rendering and three local SVG icons.
- Regression tests for links, statements, and profiles.

Verification (2026-10-29):
- `python -m pytest openlibrary/tests/core/test_wikidata.py -q -o reruns=0`: exit 0, 14 passed.
- `ruff check openlibrary/core/wikidata.py openlibrary/tests/core/test_wikidata.py`: exit 0.
- `git diff --check`: exit 0.
- `web.template.frender` on author infobox and `ElementTree.parse` on all three icons: exit 0.

Tooling: `rg` was unavailable (`/bin/bash: rg: command not found`); local inspection used `find`/`grep`.
