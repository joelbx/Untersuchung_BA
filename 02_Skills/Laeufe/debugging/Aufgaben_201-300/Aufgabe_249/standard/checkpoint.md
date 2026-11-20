# Checkpoint

Task: Add structured external profiles to WikidataEntity and display them in the author infobox.

Current phase: root cause investigation. `rg` is unavailable (`/bin/bash: rg: command not found`), so repository discovery will use `find` and `grep`.

Root cause: WikidataEntity has no sitelink, statement, or profile methods. Author.wikidata() has an unconditional early `return None`, so the infobox cannot receive cached entity data. The infobox only renders a description and has no profile markup. Existing icon assets for the required URLs are absent.

Pattern: REST entity data is held in `sitelinks` and `statements` dictionaries; the existing infobox gets a locale with `i18n.get_locale()` and calls `page.wikidata()`.

Hypothesis: Adding extraction methods to the entity and restoring Author.wikidata() will expose the profiles; rendering `get_external_profiles(i18n.get_locale())` in the infobox will display them. Focused tests were added and run first: `python -m pytest openlibrary/tests/core/test_wikidata.py -q` failed with the three expected AttributeErrors (7 existing tests passed).

Implementation: Added language-aware Wikipedia sitelink lookup, statement content extraction, and structured Wikipedia/Wikidata/Google Scholar profiles. Removed the premature return from Author.wikidata(), rendered profiles in the author infobox, and added the three SVG files used by its icon URLs. A focused author lookup test first failed on the premature return. A malformed `None` content case first failed, then was filtered.

Verification: `python -m pytest openlibrary/tests/core/test_wikidata.py openlibrary/tests/core/test_models.py -q` passed (36 tests). `python -m ruff check openlibrary/core/wikidata.py openlibrary/core/models.py openlibrary/tests/core/test_wikidata.py` and `git diff --check` passed. The infobox template compiled, all three SVGs parsed, and a render smoke test contained Wikipedia, Wikidata, and Google Scholar links. Existing pytest dependency deprecation warnings and a statsd configuration message did not affect exit codes.
