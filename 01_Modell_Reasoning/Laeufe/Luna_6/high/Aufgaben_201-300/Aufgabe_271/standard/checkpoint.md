# Checkpoint

Task: Fix ImportAPI publisher/place parsing and ISBN length classification per the issue requirements.

Implemented the requested parsing changes in `openlibrary/plugins/upstream/utils.py`, moved the length-only ISBN classifier to `openlibrary/utils/isbn.py`, and updated ImportAPI to use the new parser and ISBN utility. Existing upstream helper names remain available for compatibility.

Validation: `pytest -q openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/upstream/tests/test_utils.py openlibrary/utils/tests/test_isbn.py` passed (35 tests). `git diff --check` passed. Manually exercised the reported multi-location publisher string, multiple location/publisher pairs, unidentified-place comma fallback, malformed colon segment, brackets, and ISBN trimming/length classification.
