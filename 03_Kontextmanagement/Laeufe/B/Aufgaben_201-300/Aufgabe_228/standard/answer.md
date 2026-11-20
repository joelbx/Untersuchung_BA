Implemented normalized `QVersionNumber` parsing in [utils.py](/app/qutebrowser/utils/utils.py) and updated the requested Qt checks, distribution version, and crash dialog comparisons.

The relevant tests passed: **421 passed, 4 skipped**. One unrelated `test_unpatched` case was excluded because it exited before reporting a result in this environment.