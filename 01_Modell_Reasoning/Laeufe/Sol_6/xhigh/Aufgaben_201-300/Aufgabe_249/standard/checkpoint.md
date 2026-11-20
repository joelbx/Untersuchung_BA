# Checkpoint

- Task: add structured, language-aware external profiles to Wikidata entities and display them on author infoboxes.
- Initial state: working tree clean.
- Constraints: local code and tests only; preserve git history, index baseline, and harness configuration.
- Completed: added Wikipedia fallback and statement extraction helpers, structured profiles, author lookup, infobox links, SVG icons, and focused tests.
- Verified: 38 targeted tests pass; infobox renders all profiles in a local render check; Ruff, Stylelint, SVG parsing, and git diff checks pass. Black is unavailable in the environment.
