# Checkpoint

Task: Add optional encoding validation to `FormatString` and apply ASCII validation to the user agent header setting.

Changes: `FormatString` now stores an optional `encoding`, validates input with it in `to_py` using the same validation message as `String`, and includes it in its repr. `content.headers.user_agent` now specifies `encoding: ascii`. With no encoding supplied, conversion follows the existing behavior.

Verification: `pytest -q tests/unit/config/test_configtypes.py tests/unit/config/test_configdata.py` completed with 1134 passed and 10 xfailed.
