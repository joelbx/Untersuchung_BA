# QtWebEngine feature flag investigation

Status: root cause identified. `qt_args` extracts only `--enable-features=` switches before appending generated QtWebEngine arguments. `--disable-features=` switches remain in the earlier argv segment, so the generated enable switch follows them. No module prefix constants exist. Both command-line `--qt-flag` and `qt.args` flow into the same argv list. `rg` is unavailable, so searches use `grep` and `find`.

Baseline: `python -m pytest tests/unit/config/test_qtargs.py -q` passed (82 tests). New regression tests fail for both source types because the enable switch follows the disable switch, and for absent `ENABLE_FEATURES_PREFIX`. Command: `python -m pytest tests/unit/config/test_qtargs.py -q -k 'enabled_and_disabled_features or feature_prefixes'` (exit 1, 3 failed).

Hypothesis: collecting both feature switch types from the common argv list and emitting untouched disable switches after the single merged enable switch will yield consistent behavior for either source.

Implemented: exposed `ENABLE_FEATURES_PREFIX` and `DISABLE_FEATURES_PREFIX`; collected both switch types from the shared argument list; merged enabled values into one switch and emitted disabled switches unchanged after it. Added regression tests for each source and both sources together.

Verification: `python -m pytest tests/unit/config/test_qtargs.py -q -o reruns=0` passed (86 tests). `git diff --check` passed. `python -m flake8 qutebrowser/config/qtargs.py tests/unit/config/test_qtargs.py` could not run: `/usr/local/bin/python: No module named flake8` (exit 1). Lint status is therefore unverified; no dependencies were downloaded.
