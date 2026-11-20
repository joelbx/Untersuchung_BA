Implemented message based JavaScript log filtering.

- Added `_js_log_to_ui` to check source and level eligibility, then apply source and message glob exclusions. `javascript_log_message` now falls back to the standard logger when the helper returns `False`.
- Added `content.javascript.log_message.levels` and `.excludes`, including migration from the previous setting name, and updated the settings reference and changelog.

Validation: `py_compile` and `git diff --check` passed. The focused tests reported 242 passed and 1 skipped; pytest exited nonzero during X server shutdown. Including the excluded `test_nul_bytes` also hits an unrelated Python 3.11 `SyntaxError` versus `ValueError` expectation.

Files: [shared.py](/app/qutebrowser/browser/shared.py:162), [configdata.yml](/app/qutebrowser/config/configdata.yml:946), [settings reference](/app/doc/help/settings.asciidoc), [changelog](/app/doc/changelog.asciidoc).