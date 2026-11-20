VERDICT: FIX

**Code defect:** [hostblock.py](/app/qutebrowser/components/hostblock.py:131) strips trailing dots from request hosts, but the hosts parser retains them in blocked entries. A blocklist entry of `example.com.` therefore matches neither `https://example.com/` nor `https://example.com./`. I confirmed this with a local reproduction. Normalize blocked entries when loading them, or compare normalized forms on both sides.

**Tests:** `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/components/test_hostblock.py tests/unit/utils/test_urlutils.py` — 356 passed, 1 skipped. No test environment problem. No project code was changed during this review.