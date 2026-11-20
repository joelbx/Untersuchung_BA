# Checkpoint

Task: Fix Qt 6.4 dark mode text threshold key emission.
Status: Complete.
Change: Added a Qt 6.4 definition mapping threshold.text to ForegroundBrightnessThreshold, retaining earlier mappings.
Verification: QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webengine/test_darkmode.py (42 passed); git diff --check.
