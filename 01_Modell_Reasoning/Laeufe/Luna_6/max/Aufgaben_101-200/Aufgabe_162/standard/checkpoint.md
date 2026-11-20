# Checkpoint

Issue: Add optional encoding validation to `FormatString` during `to_py`, matching the existing `String` validation behavior while retaining current behavior when no encoding is configured.

Initial state: Repository root is `/app`. No `AGENTS.md` instructions were found. `rg` is unavailable in this environment, so searches will use `find`/`grep`.

Findings and changes:
- `String` validates encodability in `to_py`; `FormatString` now uses the same shared check and accepts optional `encoding`.
- `content.headers.user_agent` now configures `encoding: ascii`, so non-ASCII templates fail at configuration conversion.
- Focused `FormatString` tests cover absent encoding, ASCII, UTF-8, and an invalid ASCII value.

Validation complete: `pytest -q tests/unit/config/test_configtypes.py tests/unit/config/test_configdata.py` passed (1,138 passed, 10 xfailed). `git diff --check` passed.
