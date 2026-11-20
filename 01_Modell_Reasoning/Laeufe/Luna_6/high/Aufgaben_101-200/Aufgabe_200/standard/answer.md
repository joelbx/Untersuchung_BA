Implemented unit-aware durations in `:later`. `parse_duration` supports decimal hours, minutes, and seconds with optional whitespace, while bare integers remain milliseconds. Updated the existing end-to-end scenario to use `0.5s` and removed the obsolete expected-failure marker for negative delays.

The utility and util-command unit suites passed: **180 tests**. The end-to-end suite could not start because `PyQt5.QtWebKit` is unavailable in the environment.

Changes are in [utils.py](/app/qutebrowser/utils/utils.py), [utilcmds.py](/app/qutebrowser/misc/utilcmds.py), and the duration tests and feature scenario. `git diff --check` passed.