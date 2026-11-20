# Checkpoint

Task: add structured external profiles to `WikidataEntity` and display them on the author infobox.

Plan: inspect local model, template, and existing tests; implement language fallback and statement extraction; run relevant existing tests.

Status: implemented Wikipedia language fallback, resilient statement extraction,
structured Wikidata and Google Scholar profiles, infobox rendering, and icons.
Added focused tests. `pytest -q openlibrary/tests/core/test_wikidata.py` passed
(12 tests); Ruff, template compilation, SVG parsing, and `git diff --check` passed.
No delegation used.
