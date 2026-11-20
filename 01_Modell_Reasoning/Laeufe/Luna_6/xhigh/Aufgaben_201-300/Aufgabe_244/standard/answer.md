Implemented the foreground threshold option with default `256`. QtWebEngine versions before 6.4 use `TextBrightnessThreshold`; 6.4+ use `ForegroundBrightnessThreshold`. Existing `threshold.text` settings migrate to the new option.

Updated the generated settings reference and added coverage for version selection and config migration in [darkmode.py](/app/qutebrowser/browser/webengine/darkmode.py), [configdata.yml](/app/qutebrowser/config/configdata.yml), and the relevant test files.

**Verification:** 269 passed, 1 skipped in the dark mode and config file tests; 31 passed in config data tests. `git diff --check` passed. Tests ran with `QT_QPA_PLATFORM=offscreen`.