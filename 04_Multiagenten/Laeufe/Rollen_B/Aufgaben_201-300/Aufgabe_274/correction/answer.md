The current patch meets the requested behavior. The reviewer found no code defect, so no project code changes were needed in this correction round.

With `QT_QPA_PLATFORM=offscreen`, the previously interrupted tests passed: 111 in `test_qtargs.py` and 31 in `test_configdata.py`. `git diff --check` also passed. The initial display failure was a **TEST_ENVIRONMENT_PROBLEM**.