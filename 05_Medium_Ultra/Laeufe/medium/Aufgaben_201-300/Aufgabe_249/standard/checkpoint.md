Task: Add structured Wikidata external profiles and display them on author infobox.
Status: Complete. Added Wikipedia fallback, statement extraction, structured profiles, author infobox display, and three SVG icons. Added tests for fallback, malformed statements, and multiple Google Scholar IDs.
Verification: pytest -q openlibrary/tests/core/test_wikidata.py (13 passed); ruff check on changed Python files (passed); infobox template compiled; git diff --check (passed).
