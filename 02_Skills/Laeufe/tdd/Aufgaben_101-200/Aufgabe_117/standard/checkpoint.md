# Checkpoint

Implemented opt-in `qt.workarounds.locale` (QtWebEngine only, default false), locale pack lookup, Chromium locale fallbacks, and `--lang` startup argument for Linux QtWebEngine 5.15.3. Added test-first coverage in `tests/unit/config/test_qtargs.py`; observed a correct red failure for the missing option and another for the final `en-US` fallback before implementing each behavior.

Verification:
- `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_configdata.py tests/unit/config/test_qtargs.py --reruns 0`: 182 passed.
- `git diff --check`: passed.
- `python -m compileall -q qutebrowser/config/qtargs.py tests/unit/config/test_qtargs.py`: passed.

Broader checks attempted:
- `pytest -q tests/unit/config/test_qtargs.py -k 'locale_'`: Qt aborted at QApplication creation because there is no display. Re-ran with `QT_QPA_PLATFORM=offscreen` successfully.
- `QT_QPA_PLATFORM=offscreen pytest --reruns 0 -q`: exited 1. End-to-end tests `test_adblock[auto]`, `test_adblock[hosts]` and others error during setup because the installed pytest-qt has no `pytestqt.plugin.SignalBlocker` attribute. The full run did not complete, so the full suite status remains unknown.
- `QT_QPA_PLATFORM=offscreen pytest tests/unit --reruns 0 -q`: exited 1 after `tests/unit/browser/test_caret.py`; no explicit error in captured output. Unit suite status remains unknown.
- `QT_QPA_PLATFORM=offscreen pytest tests/unit/config --reruns 0 -q`: exited 1. `tests/unit/config/test_configfiles.py::TestConfigPy::test_nul_bytes` fails because Python 3.11 raises `SyntaxError` for NUL bytes while the test expects `ValueError`. The process output stopped near `test_websettings.py`; complete config suite status remains unknown.
