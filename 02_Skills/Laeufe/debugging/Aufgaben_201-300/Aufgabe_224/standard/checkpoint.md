# Checkpoint

Investigating the reported color interpolation crash. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` for code search.

Root cause: `_get_color_percentage` and `interpolate_color` exist only in `utils.py`; the required `qtutils.interpolate_color` interface is absent, while progress callers still target `utils`. A new Qt utility test reproduced `AttributeError` (3 selected cases failed). Hypothesis: relocating the implementation and updating all three call sites resolves the module mismatch. The original `None` colorspace branch also bypasses percentage validation and returns RGB regardless of start spec, so preserving the stated interface needs those two corrections.

Implementation: moved both functions to `qtutils.py`, updated download and tab progress callers, and moved interpolation tests to `test_qtutils.py`. Added coverage for the new module interface, out-of-range percentages with `colorspace=None`, and preserving the start color spec.

Verification: `QT_QPA_PLATFORM=offscreen xvfb-run -a python3 -m pytest -q -p no:xvfb --reruns 0 tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py tests/unit/browser/test_downloads.py tests/unit/mainwindow/test_tabbedbrowser.py` exited 0: 336 passed. `git diff --check` exited 0.

Tooling notes: `python3 -m flake8 qutebrowser/utils/qtutils.py qutebrowser/utils/utils.py qutebrowser/browser/downloads.py qutebrowser/mainwindow/tabbedbrowser.py tests/unit/utils/test_qtutils.py tests/unit/utils/test_utils.py` exited 1 with `/usr/local/bin/python3: No module named flake8`; lint status remains unverified. A direct pytest invocation with the xvfb plugin reported 307 passed but exited 1 with `XIO: fatal IO error 0 (Success) on X server ":0"`; disabling that plugin without a display failed with `Exception: No display and no Xvfb available!`. The final xvfb-run command above resolved the test environment and passed.
