# Fault localization progress

Inspected `qutebrowser/config/qtargs.py`, `qutebrowser/qutebrowser.py`, `qutebrowser/app.py`, configuration metadata, and `tests/unit/config/test_qtargs.py`. No project source or tests changed.

- `qt_args` builds one argv from `--qt-flag`, `--qt-arg`, and `qt.args` (qtargs.py:41-50). Both sources therefore feed the same WebEngine processing path.
- WebEngine processing extracts only `--enable-features=` values, removes them, then lets `_qtwebengine_args` emit one merged enable flag (qtargs.py:56-59,160-162). `_qtwebengine_enabled_features` splits comma lists and injects features such as `OverlayScrollbar` (qtargs.py:64-120).
- `--disable-features=` has no named prefix constant, dedicated recognition, or tests. When supplied through `--qt-flag disable-features=...` or `qt.args`, its string remains in argv unchanged by the Python builder. The reported effective-feature failure cannot be localized beyond the QtWebEngine handoff from static code alone.
- The application parser has no direct `--disable-features` option; it accepts `--qt-flag`/`--qt-arg` (qutebrowser.py:120-126) and calls `parse_args` (line 189). The constructed argv is passed to QApplication (app.py:522-526).
- Existing `test_overlay_features_flag` covers only enable flags across command line and config (test_qtargs.py:344-384). `python -m pytest tests/unit/config/test_qtargs.py -q` passed: 82 tests.

Likely implementation focus: `qutebrowser/config/qtargs.py` feature flag classification and `_qtwebengine_args`; add module constants for both exact prefixes, preserve disable flag text as a separate argument, and verify combined enable/disable behavior from each source. Clarify whether a bare direct `--disable-features=...` is in scope, since the parser currently rejects it. Downstream QtWebEngine interpretation remains uncertain without an integration observation.
