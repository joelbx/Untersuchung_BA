Task: Fix GUI process startup error messages to include process name, exact command, error type and detail, with Unix executable hint for missing/denied commands.
Status: Complete. Updated qutebrowser/misc/guiprocess.py and tests/unit/misc/test_guiprocess.py.
Verification: DISPLAY=:99 QT_QPA_PLATFORM=offscreen pytest -p no:xvfb -q --reruns 0 --tb=short tests/unit/misc/test_guiprocess.py (29 passed, exit 0); git diff --check passed.
