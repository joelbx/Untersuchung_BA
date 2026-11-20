Fixed the reviewer’s test defect: the cutoff test now uses a separate topic, so it no longer changes the shared topic’s post index.

The reviewer’s checks pass: 12 voting tests, 127 tests in `test/posts.js`, ESLint, and `git diff --check`. The first test attempt hit **TEST_ENVIRONMENT_PROBLEM** because local Redis was stopped; after starting the installed service, both test commands passed.