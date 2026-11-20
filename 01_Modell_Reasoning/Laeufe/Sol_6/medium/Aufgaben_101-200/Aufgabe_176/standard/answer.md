Updated [incdec_number](/app/qutebrowser/utils/urlutils.py:549) to skip digits inside percent escapes, preserve encoded URL data and zero padding, reject invalid counts and decrements below zero, and leave ports untouched. Added coverage in [test_urlutils.py](/app/tests/unit/utils/test_urlutils.py:619).

The focused tests pass: **197 passed**. The full test file aborted during Qt application setup, including under `xvfb-run`.

The issue gives conflicting selection rules. I retained the existing last-match behavior, which matches the earlier requirements and existing tests.