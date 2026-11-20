Issue: add message-content exclusions to JavaScript UI log filtering.

Implemented: added `_js_log_to_ui` with source/level eligibility and source/message glob exclusions; added `content.javascript.log_message.levels` and `.excludes`; migrated the old setting name; updated settings documentation and changelog.

Validation: `tests/unit/browser/test_shared.py` passed (6 tests) and `tests/unit/config/test_configdata.py` passed (31 tests) with `QT_QPA_PLATFORM=offscreen`. A plain pytest attempt aborted at Qt application startup in this headless environment.

Constraints: use repository code/tests only; do not change the git index baseline, history, or harness configuration.
