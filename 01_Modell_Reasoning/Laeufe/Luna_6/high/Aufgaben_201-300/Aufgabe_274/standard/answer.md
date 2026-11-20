Implemented version-aware canvas workaround modes.

- [configdata.yml](/app/qutebrowser/config/configdata.yml) now accepts `always`, `auto`, and `never`, with `auto` as the default.
- [qtargs.py](/app/qutebrowser/config/qtargs.py) resolves `auto` to `always` only on Qt 6 with a known Chromium major below 111, and passes the required context into the settings mapper.

Verification: all 102 tests in `tests/unit/config/test_qtargs.py` passed with Qt’s offscreen platform. Syntax and diff checks passed.