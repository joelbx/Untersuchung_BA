# Checkpoint

Task: add version-aware `qt.workarounds.disable_accelerated_2d_canvas` modes.
Status: implemented and verified.
Changes: string enum with auto default; auto resolver uses runtime Qt 6 and known Chromium major below 111; WebEngine settings receive version, CLI namespace, and special flags; boundary tests added.
Tests: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py` (111 passed); `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_configdata.py` (31 passed).
Note: plain pytest aborted during Qt application creation because no display platform was configured. Offscreen run passed.
Delegation: none.
