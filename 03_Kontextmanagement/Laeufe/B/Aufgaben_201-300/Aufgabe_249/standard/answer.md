Implemented language-aware Wikipedia links, Wikidata and Google Scholar profile entries, and their display in the author infobox. The new [profile methods](/app/openlibrary/core/wikidata.py) handle missing or malformed statements and multiple Scholar IDs.

Verification: all 10 Wikidata tests passed, and `git diff --check` passed.