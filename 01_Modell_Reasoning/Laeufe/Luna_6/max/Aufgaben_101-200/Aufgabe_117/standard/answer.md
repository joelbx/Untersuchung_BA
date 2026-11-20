Implemented `qt.workarounds.locale` as a `false` by default, QtWebEngine-only setting. On Linux with QtWebEngine 5.15.3, enabling it checks for the current locale’s pack and adds `--lang` when a Chromium-compatible fallback is needed.

Locale lookup and fallback logic are in [qtargs.py](/app/qutebrowser/config/qtargs.py:221); the setting is in [configdata.yml](/app/qutebrowser/config/configdata.yml:314).

Verification: the existing config tests passed, **148 passed**, using `QT_QPA_PLATFORM=offscreen`. `git diff --check` is clean.