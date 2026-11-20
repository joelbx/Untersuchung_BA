Implemented structured Wikidata profiles and displayed them in the author infobox. Wikipedia links use the requested language with English fallback; Google Scholar identifiers from P1960 produce one profile per valid identifier. I also restored the author’s Wikidata cache lookup so the infobox can access entities.

Added the required SVG icons and infobox styling.

Verification passed: 7 Wikidata tests, 25 model tests, Ruff, and `git diff --check`.