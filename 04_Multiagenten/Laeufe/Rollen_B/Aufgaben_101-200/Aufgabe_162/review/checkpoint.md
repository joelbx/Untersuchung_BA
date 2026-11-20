VERDICT: ACCEPT
Reviewed the applied patch in qutebrowser/config/configtypes.py and qutebrowser/config/configdata.yml with its existing test changes. FormatString accepts optional encoding, validates input in to_py with ValidationError, and user_agent requires ascii. No correctness or regression defect found.
Tests: pytest -q tests/unit/config/test_configtypes.py -k 'FormatString' tests/unit/config/test_configdata.py -k 'FormatString or user_agent_encoding or test_data' => 27 passed, 1121 deselected. pytest -q tests/unit/config/test_configtypes.py tests/unit/config/test_configdata.py => 1138 passed, 10 xfailed. git diff --check => passed.
TEST_ENVIRONMENT_PROBLEM: none.
