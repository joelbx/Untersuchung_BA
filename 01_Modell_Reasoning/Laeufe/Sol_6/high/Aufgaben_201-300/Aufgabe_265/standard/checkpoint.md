# Checkpoint

Task: Correct QtColor parsing for HSV/HSVA hue percentages and validate color function names/counts.

Completed:
- Updated `_parse_value` to scale hue with 359 and other channels with 255; percentage arithmetic preserves 100% endpoints.
- Updated `to_py` to validate rgb/rgba/hsv/hsva names and arities before converting components and dispatch to the correct QColor constructor.
- Expanded existing QtColor tests for hue, RGB/A percentages, and invalid names/counts.

Verification:
- `pytest -o addopts='' -o filterwarnings='' -q tests/unit/config/test_configtypes.py -k TestQtColor`: 35 passed.
- Broader configtypes run hit pre-existing Hypothesis fixture health-check failures; non-Hypothesis run reached 793 passes, then failed in unrelated QtFont test due to PyQt rejecting a float weight.
- `git diff --check`: passed.
