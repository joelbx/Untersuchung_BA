Added `chat:privileged` to the expected privilege set in [test/middleware.js](/app/test/middleware.js:78), fixing the reviewer’s timeout.

The messaging suite passes (79 tests). The combined middleware and controller run passes 152 tests, with one remaining failure in the unrelated user data export test at [test/controllers.js](/app/test/controllers.js:1692). Running controllers alone reproduces that same failure (140 passing, 1 failing). `git diff --check` is clean.

**TEST_ENVIRONMENT_PROBLEM:** Local Redis was initially unavailable. Starting the existing Redis server resolved that issue before the test reruns.