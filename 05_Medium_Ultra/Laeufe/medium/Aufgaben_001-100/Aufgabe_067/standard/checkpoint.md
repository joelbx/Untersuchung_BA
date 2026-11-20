# Checkpoint

Task: Add `scrolling.bar=overlay`, gate its Chromium flag by QtWebEngine, Qt >= 5.11, and non-macOS; migrate legacy `False` to `overlay`; support `js_headers` test marker.

Initial findings: option lives in `qutebrowser/config/configdata.yml`; Qt arguments in `qutebrowser/config/configinit.py`; boolean migration in `qutebrowser/config/configfiles.py`. Next: inspect test fixtures and marker handling, implement, and run focused existing tests.

Completed: added the option, gated Chromium flag, migration, docs, unit coverage, and `@js_headers` collection/skip handling. The header marker skips QtWebEngine on runtime Qt 5.12 through 5.14, matching the existing WebEngine settings workaround. The BDD tag order matters: `@js_headers` must follow `@qtwebkit_skip` for both markers to survive collection.

Verification: 36 focused Qt argument tests passed; 10 migration/config data tests passed; both tagged BDD scenarios collected with `-m js_headers`; `compileall` and `git diff --check` passed. The unit test runner exits with an XIO error after reporting passes because the bundled Xvfb instance shuts down badly in this environment. End-to-end scenarios were collected, not executed.
