# Checkpoint

Task: Fix QtColor parsing so HSV hue percentages scale to 359 while other percentages scale to 255, and validate function names/component counts.

Changes made:
- `QtColor._parse_value` now accepts a hue flag and scales percentages by 359 for hue and 255 for other channels. It multiplies before dividing so 100% reaches the exact maximum.
- `QtColor.to_py` validates supported function names and component counts before parsing, then dispatches HSV/HSVA to `QColor.fromHsv` and RGB/RGBA to `QColor.fromRgb`.
- Updated QtColor regression cases for percentage hue and invalid HSV/HSVA component counts.

Verification:
- `pytest -o addopts='' -q tests/unit/config/test_configtypes.py::TestQtColor`: 27 passed.
- Full `tests/unit/config/test_configtypes.py` run was attempted. It exposed unrelated environment/test compatibility failures (Hypothesis function-scoped fixture checks, Qt/font mismatches, and other existing failures); QtColor's 100% case initially revealed and led to fixing a floating-point truncation edge case.
- `git diff --check`: passed.
