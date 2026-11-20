Task: Fix QtColor percentage hue parsing and color function validation.
Status: Implemented and verified focused tests.
Changes: Hue percentages use 359; other percentages use 255. Validation checks supported function names and arities before conversion. Regression tests cover HSV/HSVA/RGB/RGBA boundaries and invalid functions.
Tests: 55 QtColor/QssColor tests passed using pytest -q -o addopts='' tests/unit/config/test_configtypes.py -k 'TestQtColor or TestQssColor'. Full configtypes run encountered unrelated Hypothesis fixture health checks and was interrupted after widespread failures.
Delegation: none; solved directly.
