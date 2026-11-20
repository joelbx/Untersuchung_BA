Implemented `utils.parse_duration` for bare millisecond integers and `h`, `m`, and `s` components, including decimals and spaces. Updated `:later` to parse duration strings and report invalid input as a command error.

Added parser tests. `python -m pytest tests/unit/utils/test_utils.py -q` passed: 176 tests. `git diff --check` passed.