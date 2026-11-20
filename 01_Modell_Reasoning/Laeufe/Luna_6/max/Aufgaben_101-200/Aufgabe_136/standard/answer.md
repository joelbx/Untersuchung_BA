Implemented the certificate wrapper fixes:

- [WebKit wrapper](</app/qutebrowser/browser/webkit/certificateerror.py:34>) accepts `errors` and an optional named `reply`. It stores the reply without network calls during construction, escapes message content, and renders one error as a paragraph or multiple errors as a list.
- [Shared wrapper API](</app/qutebrowser/utils/usertypes.py:484>) now tracks accept/reject decisions and provides deferral behavior with `UndeferrableError`.
- [WebEngine wrappers](</app/qutebrowser/browser/webengine/certificateerror.py:53>) now provide Qt 5 and Qt 6 implementations and a version-based factory; the WebEngine handlers use those decisions.

**Validation:** 58 relevant tests passed with a clean exit, and `git diff --check` passed. The 25 WebEngine tab tests also passed, but pytest exited 1 afterward due to an X11 teardown error in this environment.