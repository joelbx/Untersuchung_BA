VERDICT: FIX
Review complete. Relevant tests: `pytest -q openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/catalog/add_book/tests/test_load_book.py openlibrary/plugins/importapi/tests` — 194 passed, exit 0. No test environment problem.
Code defects:
1. Matched-edition preview skips the cover branch in `update_edition_with_rec_data` (`save` guard, __init__.py:870), so an allowed cover that would upload and modify the edition/work in a real import leaves preview edits/status unchanged. Keep preview side-effect free while representing the proposed cover changes.
2. `find_entity` merges remote_ids and `author_import_record_to_author` adds death_date (`load_book.py:257-260, 305-313`), but `load_author_import_records` appends only keyless authors to `edits` (`__init__.py:231-249`). Existing author modifications are omitted from preview and save_many. Track changed matched authors and include them in edits.
No project code or tests changed by this review.
