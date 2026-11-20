VERDICT: ACCEPT
Reviewed qutebrowser/config/qtargs.py and tests/unit/config/test_qtargs.py against the feature flag requirements. No correctness or regression issue found. Both prefixes have the required literals; enable flags are merged into one entry with injected features; disable flags retain their original strings and separate entries across command line and configuration.
Test: python -m pytest -q tests/unit/config/test_qtargs.py — 84 passed in 0.85s (exit 0).
Check: git diff --check — passed (exit 0).
