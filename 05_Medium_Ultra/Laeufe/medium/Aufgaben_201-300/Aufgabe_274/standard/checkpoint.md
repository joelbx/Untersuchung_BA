Task: Support version-aware modes for qt.workarounds.disable_accelerated_2d_canvas.
Status: Complete.
Changes: Migrated schema to always/auto/never with auto default; passed WebEngine versions, namespace, and special flags to setting resolver; added Qt and Chromium boundary tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py (144 passed); git diff --check passed.
