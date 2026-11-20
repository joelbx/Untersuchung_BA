# Progress checkpoint

- Task: normalize IA publisher/place and ISBN fields in `get_ia_record`, with public upstream utilities.
- Initial state: clean working tree; relevant code and tests are under `openlibrary/plugins/upstream` and the IA import modules. No `AGENTS.md` found.
- Implemented `get_isbn_10_and_13` and `get_publisher_and_place` in upstream utilities; `get_ia_record` now uses their normalized fields and omits empty ones.
- Updated import tests and added utility coverage for strings, lists, whitespace, mixed entries, and empty values.
- Verified: `pytest -q openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py` (33 passed); `git diff --check` passed.
