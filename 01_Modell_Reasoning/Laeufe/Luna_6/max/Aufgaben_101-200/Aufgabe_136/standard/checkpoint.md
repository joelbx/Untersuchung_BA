# Checkpoint

Task: Resolve the WebKit certificate error wrapper constructor and HTML rendering issue, including the listed shared and WebEngine certificate decision interfaces.

Implemented:
- Added certificate decision state, accept/reject/defer APIs, and `UndeferrableError` to the shared wrapper.
- Updated WebKit wrapper to accept `errors` and optional named `reply`, defer network actions until acceptance, and render escaped paragraph/list HTML.
- Added Qt 5/Qt 6 WebEngine wrappers and a version-based factory; routed the WebEngine decision flow through them.

Validation:
- 83 selected existing tests passed.
- Pytest exits with status 1 after the passing summary because Qt/Xvfb teardown emits an XIO fatal error in this environment. `QTWEBENGINE_DISABLE_SANDBOX=1` was needed for the Chromium test fixture running as root.
