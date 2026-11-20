# Checkpoint

Task: Fix certificate error wrappers and HTML rendering in the checked-out repository.

Initial state: The WebKit wrapper accepts only `errors`; its HTML path uses the abstract base for a single error and Jinja for multiple errors. The WebEngine wrapper has one class. The original WebKit HTML tests passed (4 tests).

Changes completed: Added shared decision methods and `UndeferrableError`; WebKit reply support and explicit escaping; Qt5/Qt6 WebEngine wrappers and factory; integrated decisions into network manager, WebEngine tab, and page. Added tests for HTML escaping, deferred network effects, state, and Qt version decisions.

Verification: Focused suite passed (27 tests). Existing WebEngine tab tests reported 25 passing tests when `QTWEBENGINE_DISABLE_SANDBOX=1`, but their runner exited 1 during X11 teardown. `git diff --check` passed. Qt6 is not installed locally, so the Qt6 wrapper was tested with a fake Qt error object.
