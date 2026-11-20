Task: Resolve certificate error wrapper constructor, HTML rendering, and related WebEngine interfaces.
Status: Implemented and verified.
Changes: WebKit reply/errors constructor compatibility and reply decision methods; shared certificate decision API and UndeferrableError; Qt5/Qt6 WebEngine wrappers and factory; callers updated; focused tests added.
Verification: 10 focused/network tests passed. 25 WebEngine tab tests reported passed with QTWEBENGINE_DISABLE_SANDBOX=1, but pytest exited 1 after an X11 disconnect during teardown. git diff --check passed. flake8 unavailable locally.
Constraints: Local code/tests only; git history, index baseline, and harness configuration untouched.
