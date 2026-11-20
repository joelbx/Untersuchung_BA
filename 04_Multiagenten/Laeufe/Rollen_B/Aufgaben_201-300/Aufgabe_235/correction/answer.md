Fixed the reviewed MARC author normalization defect: `Smith [from old catalog].` now becomes `Smith` in both `name` and `personal_name`, while periods in other name parts are preserved. Added regression coverage.

Both reviewer flagged commands passed: 61 tests in `test_parse.py` and 122 tests across the MARC test directory. `git diff --check` also passed.