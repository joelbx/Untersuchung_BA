# Checkpoint

Task: Resolve FormatString missing encoding validation for HTTP header configuration.

Changes:
- Shared String's encoding validation helper on BaseType.
- Added optional `encoding` to FormatString and validate values in `to_py` before placeholder parsing.
- Configured `content.headers.user_agent` to require ASCII.

Validation:
- `pytest -q tests/unit/config/test_configtypes.py tests/unit/config/test_configdata.py`
- Result: 1,134 passed, 10 xfailed.
