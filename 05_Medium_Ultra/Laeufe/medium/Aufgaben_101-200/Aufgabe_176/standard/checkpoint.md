Task: Fix incdec_number URL numeric handling in qutebrowser/utils/urlutils.py.
Status: Completed implementation and regression tests.
Behavior: Search the first eligible number in path, query, anchor, host order; skip percent-encoded triplets; never modify ports; default to path; validate operation/count; reject negative decrements; preserve zero padding and encoded segment text.
Verification: QT_QPA_PLATFORM=offscreen pytest -q -o addopts='' tests/unit/utils/test_urlutils.py => 375 passed, 1 skipped. git diff --check passed.
Note: The issue contains conflicting first/last match wording; implemented its final, explicit first-match rule.
