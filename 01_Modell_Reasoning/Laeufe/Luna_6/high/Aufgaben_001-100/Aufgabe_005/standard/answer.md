Implemented the Qt startup and error handling changes across [machinery.py](/app/qutebrowser/qt/machinery.py), [earlyinit.py](/app/qutebrowser/misc/earlyinit.py), and [qutebrowser.py](/app/qutebrowser/qutebrowser.py). `machinery.init()` now returns `SelectionInfo`; implicit initialization autoselects and raises `NoWrapperAvailableError` if no wrapper imports. Early initialization passes that info to `check_qt_available()` and logs it at debug level.

Added coverage for the error message, selection formatting, returned info, and checker diagnostics.

**Validation:** 39 focused tests passed, and `git diff --check` passed. The full version test module exited with code 1 before producing a pytest summary; its focused `test_version_info` cases passed.