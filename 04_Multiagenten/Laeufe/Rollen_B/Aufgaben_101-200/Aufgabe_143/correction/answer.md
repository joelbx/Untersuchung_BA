Fixed the failing field-transfer fixture to use a list of author dictionaries and verify that expansion adds the author identifier.

Both test commands from the review now pass: 56 passed in `test_utils.py`; 72 passed, 1 xfailed, and 2 xpassed in the matching suite. `git diff --check` is clean. TEST_ENVIRONMENT_PROBLEM: none.