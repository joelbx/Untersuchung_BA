Task: Support version-aware modes for qt.workarounds.disable_accelerated_2d_canvas.
Status: Completed schema migration, version-aware resolver, argument forwarding, and boundary tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py (113 passed); QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_configdata.py tests/unit/config/test_configfiles.py (259 passed, 1 skipped); git diff --check passed.
