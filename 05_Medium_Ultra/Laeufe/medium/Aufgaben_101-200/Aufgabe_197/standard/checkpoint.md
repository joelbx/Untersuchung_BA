# Checkpoint

Task: correct Qt 6.4 text brightness threshold key.
Status: implemented Qt 6.4 variant and regression coverage.
Verification: QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/browser/webengine/test_darkmode.py -q (40 passed); git diff --check passed.
