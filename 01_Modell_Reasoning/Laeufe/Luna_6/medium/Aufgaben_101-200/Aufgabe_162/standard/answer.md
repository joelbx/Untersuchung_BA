Implemented optional `encoding` validation for `FormatString` and configured the user agent header to require ASCII. Added tests for valid ASCII, rejected non-ASCII, and backward-compatible behavior without an encoding constraint.

Verification: `tests/unit/config/test_configtypes.py` passed (1106 passed, 10 xfailed); `git diff --check` passed.