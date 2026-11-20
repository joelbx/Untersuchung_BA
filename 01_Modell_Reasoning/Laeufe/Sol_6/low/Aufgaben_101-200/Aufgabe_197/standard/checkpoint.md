# Checkpoint
Task: fix Qt 6.4 text dark mode threshold key.
Status: complete.
Changed: Qt 6.4 variant emits ForegroundBrightnessThreshold; older variants retain TextBrightnessThreshold.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py (40 passed).
