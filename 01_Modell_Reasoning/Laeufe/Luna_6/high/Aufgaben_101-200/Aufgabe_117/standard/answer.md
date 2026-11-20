Implemented the `qt.workarounds.locale` setting and QtWebEngine `--lang` fallback for Linux with QtWebEngine 5.15.3. It checks for the exact locale `.pak` first, then applies Chromium locale mappings and fallbacks.

Validation passed: 148 focused config and Qt argument tests, plus `git diff --check`. Tests required `QT_QPA_PLATFORM=offscreen` in this headless environment.