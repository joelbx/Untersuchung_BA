Updated the version-specific dark mode mapping so Qt 6.4 emits `ForegroundBrightnessThreshold` with the numeric text threshold converted to a string. Qt 6.3 retains `TextBrightnessThreshold`.

Verification: the regression test reproduced the Qt 6.4 failure before the change; afterward, all 40 tests in the dark mode test file passed.