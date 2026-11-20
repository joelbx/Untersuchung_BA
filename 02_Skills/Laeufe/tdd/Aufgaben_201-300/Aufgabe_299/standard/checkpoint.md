# Checkpoint

Task: Add filesystem path completion to `:open`.

Implemented `FilePathCategory`, URL model registration, `completion.open_categories` and `completion.favorite_paths`, help text, and regression tests. Test-first red runs observed missing option, invalid `filesystem` value, and bare-tilde behavior before implementation. Existing quickmark/bookmark expectations were updated for the new default empty Filesystem category.

Checks:
- `QT_QPA_PLATFORM=offscreen xvfb-run -a pytest -p no:xvfb -q --reruns 0 tests/unit/completion`: 297 passed, 1 skipped, 1 xfailed; exit 0.
- `QT_QPA_PLATFORM=offscreen xvfb-run -a pytest -p no:xvfb -q --reruns 0 tests/unit/config/test_configdata.py`: 31 passed; exit 0.
- `QT_QPA_PLATFORM=offscreen xvfb-run -a pytest -p no:xvfb -q --reruns 0 tests/unit/completion/test_models.py tests/unit/config/test_configdata.py`: 109 passed; exit 0.
- `python -m py_compile qutebrowser/completion/models/filepathcategory.py qutebrowser/completion/models/urlmodel.py tests/unit/completion/test_models.py`: exit 0.
- `git diff --check`: exit 0.

Broader checks and limits:
- `QT_QPA_PLATFORM=offscreen pytest --reruns 0 -q` was started and interrupted after 88.49 seconds because end-to-end tests repeatedly could not import QtWebKit from PyQt5. At interruption: 14 failed, 167 passed, 18 skipped, 1 xfailed, 217 errors, 7 reruns. Failures included `tests/end2end/test_invocations.py` (startup-dependent cases and `test_version`) and `tests/end2end/test_mkvenv.py::test_smoke`; errors also occurred in end-to-end feature tests and `test_dirbrowser.py`, `test_hints_html.py`, `test_insert_mode.py`, and related files. Full-suite status remains unknown.
- `QT_QPA_PLATFORM=offscreen pytest --reruns 0 -q tests/unit` exited 1 without a pytest summary while entering `tests/unit/browser/test_caret.py`; it did not finish.
- `QT_QPA_PLATFORM=offscreen xvfb-run -a pytest -p no:xvfb -q --reruns 0 tests/unit/config` exited 1 without a pytest summary while entering `tests/unit/config/test_websettings.py`; config data tests passed separately.
