# Qt wrapper initialization checkpoint

- Investigating `qutebrowser/qt/machinery.py`, `qutebrowser/misc/earlyinit.py`, and their existing unit tests.
- Initial finding: machinery currently chooses the default wrapper before checking imports; autoselection raises a generic error; `init()` returns nothing.
- Startup now initializes machinery inside early initialization and passes `SelectionInfo` to the Qt checker.
- Implicit selection probes wrappers and raises `NoWrapperAvailableError` with per-wrapper reasons when none import. Successful `init()` calls return `INFO`.
- Verification: startup parser, machinery, and early initialization tests pass (58 passed); `git diff --check` and Python compilation pass.
- The broader version module run reached 152 passing tests but failed elsewhere because the installed Qt 5.15.2 lacks `QLibraryInfo.LibraryPath`, with additional Chromium version expectations failing in this environment. The changed short string format is covered by machinery tests.
