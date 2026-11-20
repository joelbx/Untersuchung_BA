# Checkpoint

Task: normalize alternate language identifiers in `format_languages` and deduplicate canonical outputs in first-seen order.

Implemented in `openlibrary/catalog/utils/__init__.py` by using the existing MARC alias map, ISO-639-1 lookup, and translated language-name resolver. Canonical language keys are validated against the site and duplicates are removed after normalization. Added a regression test covering English/native names, an ISO code, and duplicate aliases.

Verification:
- Regression test: passed (`pytest -q openlibrary/tests/catalog/test_utils.py -k format_languages_normalizes_and_deduplicates`).
- `compileall` and `git diff --check`: passed.
- Existing focused cases were also attempted, but the test process has no `web.ctx.site`; those cases fail at the pre-existing requirement for a site context.
