# Checkpoint

Task: add unit-aware duration parsing and use it in the `:later` command while preserving bare integer milliseconds.

Implemented `utils.parse_duration` for bare integer milliseconds and ordered hour/minute/second components, including decimals and whitespace. Updated `:later` to accept a duration string and schedule using the parsed milliseconds. Added utility unit cases and changed the existing `:later` end-to-end scenario to exercise `0.5s` input.

Verification: `tests/unit/utils/test_utils.py` and `tests/unit/misc/test_utilcmds.py` pass (180 tests). The `tests/end2end/features/test_utilcmds_bdd.py` run could not start qutebrowser because the configured QtWebKit backend is unavailable (`PyQt5.QtWebKit` cannot be imported).
