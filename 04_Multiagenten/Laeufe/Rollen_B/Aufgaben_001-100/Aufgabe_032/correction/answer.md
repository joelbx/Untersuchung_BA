Fixed the reviewed `async_wrapper` gaps: usage errors now include the job ID when one was supplied, and directory creation errors include the cleanup policy. Added tests for both paths.

The reviewer’s exact test command passed: **6 passed**. `git diff --check` passed. No remaining test failures or `TEST_ENVIRONMENT_PROBLEM`.