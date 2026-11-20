Task: Add content.javascript.log_message.excludes and filter JavaScript UI messages by source, level, and message glob.
Status: Complete. Added levels/excludes schema, _js_log_to_ui, logger fallback, settings help, and focused tests.
Verification: QT_QPA_PLATFORM=offscreen DISPLAY=:99 pytest -q -p no:xvfb tests/unit/browser/test_shared.py tests/unit/config/test_configdata.py --reruns 0 --disable-warnings (50 passed). git diff --check passed.
Constraints observed: Local repository only; no git history, index baseline, or harness configuration changes.
