Fixed `/lists/add` so a malformed seed index no longer causes valid indexed seeds in the same POST body to be discarded. Added a regression test for the reviewer’s case.

The reviewer’s exact test command passed: **18 passed, 1 warning**. `git diff --check` also passed. TEST_ENVIRONMENT_PROBLEM: none.