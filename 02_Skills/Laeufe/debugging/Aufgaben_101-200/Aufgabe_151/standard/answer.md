Fixed the Qt WebEngine file picker workaround. For Qt 6.2.3 through 6.6.x, it now resolves missing extensions from MIME types and wildcards, then adds them to the types passed to Qt’s picker without adding duplicate suffixes. Other Qt versions are unaffected.

Verification: all 129 WebEngine unit tests passed with offscreen Qt and the Chromium sandbox disabled for the root test environment.