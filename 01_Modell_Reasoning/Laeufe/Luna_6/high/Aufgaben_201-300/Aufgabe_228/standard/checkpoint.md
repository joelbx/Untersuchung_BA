# Checkpoint

Task: Replace specified non-Qt version parsing/comparison paths with shared `utils.parse_version` based on `QVersionNumber`.

Completed: Added normalized Qt parser; updated Qt runtime/compiled checks, QtWebKit threshold check, early Qt/PyQt minimum validation, distribution version storage, and crash dialog update note. Updated existing expectations to Qt version values.

Validation: `git diff --check` passes. `tests/unit/utils/test_qtutils.py`, `tests/unit/utils/test_utils.py`, `tests/unit/misc/test_earlyinit.py`, and `tests/unit/misc/test_crashdialog.py` pass (318 passed). `test_version.py -k 'not TestChromiumVersion'` reports 89 passed and 4 skipped; pytest then exits 1 due an X11 I/O error. The full `test_version.py` run exits during `TestChromiumVersion::test_unpatched` before pytest can report a summary; this exercises unpatched QtWebEngine startup.
