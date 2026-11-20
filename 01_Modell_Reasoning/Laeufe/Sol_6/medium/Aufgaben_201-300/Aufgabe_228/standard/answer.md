Added [utils.parse_version](/app/qutebrowser/utils/utils.py), which returns a normalized `QVersionNumber`. The Qt runtime and compiled version checks, distribution version metadata, WebKit check, and crash dialog now use Qt-native comparisons.

The 43 focused tests passed, and `git diff --check` passed. A broader test run exited before reporting a summary, so it could not be counted as passing.