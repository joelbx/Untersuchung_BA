Task: Add version-aware modes for qt.workarounds.disable_accelerated_2d_canvas.
Status: Implemented string enum/default, version-aware auto resolver, and argument forwarding. Added boundary tests for Qt 5, Qt 6.5/6.6, unknown Chromium, and Chromium 110/111.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py (144 passed).
