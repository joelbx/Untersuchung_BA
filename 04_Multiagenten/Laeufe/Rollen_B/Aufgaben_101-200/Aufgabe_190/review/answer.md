VERDICT: FIX

The patch has two correctness gaps:

- An allowed cover on a matched edition is skipped in preview because [update_edition_with_rec_data](/app/openlibrary/catalog/add_book/__init__.py:870) only processes covers when `save=True`. The preview can report the edition as matched with no edits even though a real import would modify it. Represent the proposed cover changes without uploading.
- [Author matching](/app/openlibrary/catalog/add_book/load_book.py:256) can merge remote IDs or add a death date, but [load_author_import_records](/app/openlibrary/catalog/add_book/__init__.py:231) adds only new authors to `edits`. Include modified existing authors in both preview edits and saved edits.

**Tests:** `pytest -q openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/plugins/importapi/tests` — 194 passed. These paths remain uncovered; there is no test environment problem. No project code or tests were changed during this review.