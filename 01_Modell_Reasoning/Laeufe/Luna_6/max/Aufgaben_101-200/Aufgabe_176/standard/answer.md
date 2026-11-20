Updated [`incdec_number`]( /app/qutebrowser/utils/urlutils.py:549 ) to search path, query, anchor, then host; ignore ports; default to path; preserve encoded components; validate counts and operations; and reject decrements below zero. Leading-zero behavior is preserved. Added regression coverage in [`test_urlutils.py`]( /app/tests/unit/utils/test_urlutils.py:728 ).

**Verification:** `tests/unit/utils/test_urlutils.py` passed: 353 passed, 1 skipped. `git diff --check` passed.

**QUrl limitation:** Qt normalizes escapes such as `%35` to `5` before this function receives the `QUrl`. The original encoding cannot be recovered through the existing interface.