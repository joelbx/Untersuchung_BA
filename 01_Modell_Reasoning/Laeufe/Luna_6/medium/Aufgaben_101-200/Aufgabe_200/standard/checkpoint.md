# Checkpoint

Task: add explicit hour/minute/second parsing to `:later`, retaining bare integer milliseconds.

Completed:
- Added `utils.parse_duration`, which accepts digit-only millisecond values or ordered h/m/s components (including decimals and whitespace between units) and rejects empty, negative, or malformed values.
- Updated `:later` to accept a string duration and convert it through `parse_duration` before scheduling.
- Verified requested examples and malformed inputs with direct checks.
- Ran `pytest -q tests/unit/utils/test_utils.py tests/unit/api/test_cmdutils.py`: 224 passed.
- `git diff --check` passed.
