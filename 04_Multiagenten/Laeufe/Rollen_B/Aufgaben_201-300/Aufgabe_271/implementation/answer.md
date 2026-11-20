Updated the IA fallback importer to split semicolon-separated locations from publisher names, including when the colon has no surrounding spaces. It preserves plain publisher names as a list and now classifies ISBNs by trimmed length using the helper in `openlibrary/utils/isbn.py`.

The relevant local suites passed: **34 tests**. `git diff --check` also passed.