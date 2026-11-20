# Checkpoint

Investigating ImportAPI publisher/location and ISBN parsing. External research unavailable; using local code and tests. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use grep/find.

## Root cause and hypothesis
`get_ia_record` delegates publisher metadata to `get_publisher_and_place`, which splits only on the exact delimiter `" : "` and handles only one place per input element. A multi-place value therefore remains combined or yields a single combined location. `get_isbn_10_and_13` already classifies by length but is defined in upstream utils; the requested API places it in `openlibrary.utils.isbn`. Hypothesis: a parser that distinguishes semicolon-separated places from semicolon-separated location/publisher pairs and an updated import call will satisfy the issue. The existing simple publisher cases provide the working reference.

## Verification
- Before the fix: `python -m pytest -q openlibrary/plugins/upstream/tests/test_utils.py -k 'get_location_and_publisher or get_colon_only_loc_pub'` failed as expected because both helper functions were absent (14 failures).
- After the fix: `python -m pytest -q -o reruns=0 openlibrary/plugins/importapi/tests openlibrary/plugins/upstream/tests/test_utils.py openlibrary/utils/tests/test_isbn.py` passed: 58 tests, exit code 0.
- `git diff --check` passed, exit code 0.
- Offline tooling unavailable: `python -m ruff check openlibrary/plugins/upstream/utils.py openlibrary/plugins/upstream/tests/test_utils.py openlibrary/plugins/importapi/code.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/utils/isbn.py` failed with `/usr/local/bin/python: No module named ruff`. `python -m black --check openlibrary/plugins/upstream/utils.py openlibrary/plugins/upstream/tests/test_utils.py openlibrary/plugins/importapi/code.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/utils/isbn.py` failed with `/usr/local/bin/python: No module named black`. Formatting and linting therefore remain unverified by those tools; no downloads performed.
