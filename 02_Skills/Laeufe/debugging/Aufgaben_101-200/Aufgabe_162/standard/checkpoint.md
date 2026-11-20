# Checkpoint

Investigating FormatString encoding validation in `/app`. Assigned systematic-debugging process is in use. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` for code discovery. No repository edits yet.

Root cause: `String` stores `encoding` and calls `_validate_encoding` in `to_py`; `FormatString` accepts no encoding argument and checks only placeholders. `content.headers.custom` specifies ASCII for keys and values, whereas `content.headers.user_agent` does not. A direct ad hoc import of `configtypes` failed due to a circular import, so reproduction used pytest's normal import setup. The new focused tests failed as expected: `FormatString` rejected the `encoding` constructor argument, and configured user agent accepted `ä`.

Implemented an optional `FormatString.encoding` check in `to_py`, matching the `String` validation error style. Configured `content.headers.user_agent` with `encoding: ascii`. Added tests for ASCII, Latin-1, no encoding, and the configured user agent. Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_configtypes.py tests/unit/config/test_configdata.py` exited 0 with 1138 passed, 10 xfailed, 1 rerun.
