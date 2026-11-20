Task: Add content.javascript.log_message.excludes and UI filtering helper.
Status: Implemented levels/excludes configuration, migration from old setting, UI filtering helper, documentation, and focused tests.
Verification: 42 tests passed across tests/unit/browser/test_shared.py and tests/unit/config/test_configdata.py using QT_QPA_PLATFORM=offscreen; git diff --check passed. Qt emitted an XIO shutdown message after tests.
Constraints: Local code and tests only; git history, index, and harness configuration unchanged.
