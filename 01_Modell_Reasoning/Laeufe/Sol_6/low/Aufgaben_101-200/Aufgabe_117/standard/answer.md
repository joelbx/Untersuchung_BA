Implemented `qt.workarounds.locale` as a disabled-by-default QtWebEngine setting. When enabled on Linux with QtWebEngine 5.15.3, it checks for the locale’s `.pak` file and adds `--lang` with a Chromium-compatible fallback when needed. Added tests for the mappings, fallback, gating, and argument handling.

Verification: 161 relevant tests passed; `git diff --check` passed.