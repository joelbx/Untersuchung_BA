Task: Fix `incdec_number` URL numeric matching, encoded data preservation, and decrement validation.
Status: Implemented and verified in `qutebrowser/utils/urlutils.py` with updated unit tests.
Changes: First eligible number in path, query, anchor, or host priority; port ignored; encoded escapes preserved and skipped; count and decrement bounds validated; zero padding retained.
Verification: `QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' --reruns=0 tests/unit/utils/test_urlutils.py` (425 passed, 1 skipped). `git diff --check` passed.
