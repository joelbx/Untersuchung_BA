VERDICT: ACCEPT

The applied patch adds optional encoding validation to `FormatString` and requires ASCII for `content.headers.user_agent`. I found no correctness or regression issue. No project code was changed during this review.

- `pytest -q tests/unit/config/test_configtypes.py -k 'FormatString' tests/unit/config/test_configdata.py -k 'FormatString or user_agent_encoding or test_data'`: 27 passed.
- `pytest -q tests/unit/config/test_configtypes.py tests/unit/config/test_configdata.py`: 1,138 passed, 10 xfailed.
- `git diff --check`: passed.

TEST_ENVIRONMENT_PROBLEM: none.