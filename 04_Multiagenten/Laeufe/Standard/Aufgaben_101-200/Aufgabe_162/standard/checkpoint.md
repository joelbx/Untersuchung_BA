Task: Add optional encoding validation to FormatString during to_py, consistent with String; enforce ASCII for user agent configuration.
Status: Complete. Updated FormatString, configdata.yml, and focused type/schema tests.
Verification: pytest -q tests/unit/config/test_configtypes.py tests/unit/config/test_configdata.py (1139 passed, 10 xfailed); git diff --check passed.
