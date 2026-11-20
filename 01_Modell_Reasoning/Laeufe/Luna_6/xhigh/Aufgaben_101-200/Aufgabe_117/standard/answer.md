Implemented the opt-in `qt.workarounds.locale` setting and QtWebEngine 5.15.3 locale fallback. On Linux, when enabled, qutebrowser checks the locale pack and adds a Chromium-compatible `--lang` override if the pack is missing. Updated the settings help as well.

Validation: the focused Qt argument and config data suites passed (**148 passed**) with `QT_QPA_PLATFORM=offscreen`; `git diff --check` passed. The plain headless test run aborted while initializing Qt.

Changes are in [qtargs.py](/app/qutebrowser/config/qtargs.py), [configdata.yml](/app/qutebrowser/config/configdata.yml), and [settings.asciidoc](/app/doc/help/settings.asciidoc).