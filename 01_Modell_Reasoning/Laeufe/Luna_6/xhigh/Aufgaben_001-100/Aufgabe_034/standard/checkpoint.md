# Checkpoint

Task: normalize Internet Archive publisher and ISBN metadata for `get_ia_record`.

Initial status: the working tree was clean. No `AGENTS.md` was found in the repository search. `rg` is unavailable in this environment; use `find` and standard text tools.

Plan: inspect the upstream adapter, nearby utilities and existing tests; implement the normalization while preserving other mapped fields; run the relevant existing tests.

Findings: `get_ia_record` is implemented in `openlibrary/plugins/importapi/code.py`; it currently passes through singular `publisher` and mixed `isbn`. Existing coverage is in `openlibrary/plugins/importapi/tests/test_code.py`. The requested shared utility module already has standard Python helpers and imports used by the Import API.

Implementation: add resilient publisher/place and ISBN split helpers to upstream utils, call them from `get_ia_record`, and update/add tests for canonical output and edge cases.

Completed: added `get_isbn_10_and_13` and `get_publisher_and_place`, wired both into `get_ia_record`, updated the expected edition shape, and added helper/integration coverage for mixed formats, whitespace, invalid values, and empty inputs.

Verification: `python -m pytest openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py` passed (23 tests). `git diff --check` passed.
