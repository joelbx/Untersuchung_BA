The checked-out patch already addresses the reported URL increment/decrement issues. Review found no concrete code defect, so I made no further code changes.

The reviewer’s test results reproduced with `QT_QPA_PLATFORM=offscreen` and a pytest option override: **167 increment/decrement tests passed**; the full file had **385 passed, 1 skipped**. `git diff --check` passed.

**TEST_ENVIRONMENT_PROBLEM:** This environment rejects the repository’s deprecated `--strict` pytest option. I used `--strict-markers` for the runs and left test configuration unchanged.