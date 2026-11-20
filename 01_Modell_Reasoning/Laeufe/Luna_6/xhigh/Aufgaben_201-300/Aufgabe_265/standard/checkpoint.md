# Checkpoint

Task: Correct percentage hue parsing in `QtColor` while preserving RGB/RGBA behavior and validating function names and component counts.

Completed:
- `_parse_value` now scales percentages using the component maximum; HSV hue uses 359, and other channels use 255. Multiplication occurs before division so 100% reaches the exact maximum.
- `to_py` validates function names and component counts before parsing, then calls `QColor.fromHsv` or `QColor.fromRgb` as appropriate.
- Regression coverage includes percentage and integer HSV, HSVA, RGB/RGBA, unsupported names, and invalid component counts.
- Focused test: `TestQtColor` passed (34 tests).
- Full `test_configtypes.py` run: 976 passed, 20 xfailed, 59 failed. Failures are existing environment/test compatibility issues (Hypothesis fixture health checks, Qt font API, timestamp validation); the focused color tests pass.

Final checks: `git diff --check` passed.
