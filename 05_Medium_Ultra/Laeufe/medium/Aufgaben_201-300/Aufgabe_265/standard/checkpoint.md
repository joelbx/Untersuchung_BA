Task: Fix QtColor hue percentage parsing in qutebrowser/config/configtypes.py.
Status: Implemented and verified targeted behavior.
Changes: Hue percentages scale to 359; all other percentage channels scale to 255. The parser validates color function names and argument counts before conversion, then uses QColor.fromHsv or QColor.fromRgb. Updated existing QtColor tests for HSV/HSVA and added RGB/RGBA percentage and invalid-function/count coverage.
Verification: `pytest -o addopts='' -q tests/unit/config/test_configtypes.py -k 'TestQtColor'` passed (35 tests). Full configtypes file: 978 passed, 20 xfailed, 59 unrelated failures (Hypothesis fixture health checks, Font, TimestampTemplate). `git diff --check` passed.
Constraints observed: no history/index/harness edits; local repository/tests only.
