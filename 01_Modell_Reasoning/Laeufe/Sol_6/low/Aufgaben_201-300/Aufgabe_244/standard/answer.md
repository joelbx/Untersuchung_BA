Added `colors.webpage.darkmode.threshold.foreground` as an Int option with default `256`. Saved `threshold.text` settings migrate to it. Dark mode now uses `TextBrightnessThreshold` before QtWebEngine 6.4 and `ForegroundBrightnessThreshold` from 6.4 onward.

Verification: 73 focused tests passed; the config file suite passed with 259 passed and 1 skipped.