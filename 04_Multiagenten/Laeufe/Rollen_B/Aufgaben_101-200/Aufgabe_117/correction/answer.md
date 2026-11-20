The locale workaround patch is in place. The independent review found no code defect; the interrupted test run was caused by headless Qt setup.

With `QT_QPA_PLATFORM=offscreen`, the flagged tests passed: 147 in `test_qtargs.py` and 31 in `test_configdata.py`. `git diff --check` also passed. No source changes were needed in this correction round.