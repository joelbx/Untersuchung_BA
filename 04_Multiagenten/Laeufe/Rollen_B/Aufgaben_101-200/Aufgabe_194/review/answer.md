VERDICT: FIX

I found no code defect in the signal conversion. The required signals are declared in [blockutils.py](/app/qutebrowser/components/utils/blockutils.py:58), and both consumers connect before starting downloads.

**TEST_ENVIRONMENT_PROBLEM:** The Brave blocker tests are relevant but 13 were skipped because the optional `adblock` module is absent; the skip comes from [test_braveadblock.py](/app/tests/unit/components/test_braveadblock.py:185). The review rules require FIX when relevant tests are unavailable. Rerun that existing suite in an environment where `adblock` is available.

Tests executed:

- `pytest -q tests/unit/components/test_blockutils.py` — 2 passed.
- `pytest -q tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py` — 36 passed, 13 skipped.
- `pytest -q -rs tests/unit/components/test_braveadblock.py` — 1 passed, 13 skipped.

No project code or tests were changed during this review.