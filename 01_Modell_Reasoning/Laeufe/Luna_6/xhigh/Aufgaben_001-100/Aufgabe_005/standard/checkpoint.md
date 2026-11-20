# Checkpoint

Issue: Improve Qt wrapper early initialization and diagnostics.

Implemented: Machinery returns `SelectionInfo`, autoselects during implicit initialization, raises `NoWrapperAvailableError` when no wrapper imports, records exception type names, and provides concise or detailed info formats. Startup passes `machinery.init()` state to `check_qt_available`; Qt checker diagnostics have trailing blank lines, and startup debug logging prints the selection info.

Validation: 60 focused existing tests pass, including machinery, early initialization, qutebrowser startup parsing, and version output. The full `test_version.py` run exits during its existing native Chromium version test without a pytest summary; the directly related version output test passes.
