Task: Fix the Qt 6.4 dark mode text threshold key.
Status: Fixed with a Qt 6.4 definition and regression coverage. The dark mode
unit test module passes (42 tests) with QT_QPA_PLATFORM=offscreen; git diff --check
passes.
