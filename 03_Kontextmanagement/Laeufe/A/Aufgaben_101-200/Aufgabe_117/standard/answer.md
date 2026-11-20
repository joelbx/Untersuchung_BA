Implemented `qt.workarounds.locale`, defaulting to `false` and available only with QtWebEngine. When enabled on Linux with QtWebEngine 5.15.3, it checks for the locale `.pak` file and adds a Chromium compatible `--lang` fallback when needed. Updated the [setting documentation](/app/doc/help/settings.asciidoc) and added locale and configuration tests.

Verification: 187 relevant tests passed.