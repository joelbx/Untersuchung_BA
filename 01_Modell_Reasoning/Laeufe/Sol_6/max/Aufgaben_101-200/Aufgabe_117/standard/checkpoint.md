# Checkpoint

- Task: Add the QtWebEngine 5.15.3 Linux locale workaround and configuration option.
- Implemented `qt.workarounds.locale` (off by default, QtWebEngine only), locale `.pak` path detection, Chromium compatible locale fallback, and conditional `--lang` argument.
- Updated generated settings help and changelog; added focused locale and argument tests.
- Verified: `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 python -m pytest -q --qute-bdd-webengine -k 'not test_nul_bytes' tests/unit/config` passed (1888 passed, 1 skipped, 1 deselected, 10 xfailed).
- The excluded `test_nul_bytes` expects `ValueError` from `compile()`; Python 3.11 raises `SyntaxError` here. The default backend run also failed because this environment lacks PyQt5.QtWebKit; selecting WebEngine resolved that environment issue.
