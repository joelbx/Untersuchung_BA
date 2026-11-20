# Fault localization checkpoint

Scope: inspect local Qt machinery and early initialization with existing tests; report diagnosis only. No project source or test edits.

Initial state: working tree clean. Relevant files: `qutebrowser/qt/machinery.py`, `qutebrowser/misc/earlyinit.py`, `tests/unit/misc/test_earlyinit.py`.

Findings:
- `qutebrowser/qutebrowser.py:247-248` explicitly initializes machinery before `early_init`; `early_init` currently calls `check_pyqt()` without an info argument. `check_pyqt` checks only selected `QtCore`/`QtWidgets` and exits after reporting a missing module.
- `machinery._autoselect_wrapper` records raw `ImportError` strings but raises generic `Error` after both imports fail, losing `SelectionInfo`. `_select_wrapper(None)` returns default PyQt5; `init(None)` therefore does not probe available wrappers and returns `None`.
- `SelectionInfo.__str__` always emits multiline `Qt wrapper:` plus `selected`; no short form. No debug logger in machinery currently prints `SelectionInfo`.
- Existing tests assert old generic error and old import strings; version output test embeds old verbose heading. Focused existing suite: 27 passed.

Likely fix points: `machinery.py` error class, formatting, autoselection and implicit init; `earlyinit.py` checker and initialization sequence; `qutebrowser.py` startup call site; corresponding tests and version template. Check subtle state: `_initialized` is set before selection/import validation, so failed initialization leaves guard set.
