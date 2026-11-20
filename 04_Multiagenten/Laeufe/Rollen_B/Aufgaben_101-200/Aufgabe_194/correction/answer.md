The checked-out patch implements the requested Qt signals and connects both consumers before downloads start. I found no concrete code defect, so I made no further code changes. `git diff --check` is clean.

The reviewer’s exact test commands were rerun: `test_blockutils.py` passed 2 tests; the combined adblock suites passed 36 and skipped 13; the Brave suite passed 1 and skipped 13.

**TEST_ENVIRONMENT_PROBLEM:** All 13 Brave skips are due to the missing optional `adblock` module. I could not verify those tests in this prepared environment without a download.