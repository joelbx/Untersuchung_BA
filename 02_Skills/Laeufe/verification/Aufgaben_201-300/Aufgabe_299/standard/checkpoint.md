# Checkpoint

Implemented `FilePathCategory` and registered it in the `:open` URL model. Added `completion.favorite_paths` (empty by default), enabled `filesystem` in `completion.open_categories`, regenerated settings help, and added completion tests.

Verification:
- `xvfb-run -a python3 -m pytest -q -p no:xvfb --tb=short --show-capture=no tests/unit/completion/test_models.py tests/unit/completion/test_completionmodel.py tests/unit/config/test_configdata.py` — exit 0, 106 passed.
- `python3 -c 'from scripts.dev import src2asciidoc; src2asciidoc.generate_settings("doc/help/settings.asciidoc")'` — exit 0.
- `git diff --check` — exit 0.

Tooling/earlier checks:
- `rg` unavailable: `/bin/bash: line 1: rg: command not found`; local `grep`/`find` used.
- `QT_QPA_PLATFORM=offscreen python3 -m pytest -q --tb=short --show-capture=no tests/unit/completion/test_models.py` reported 69 passed but exited 1 with `XIO: fatal IO error 0 (Success) on X server ":0"`. Replaced with explicit `xvfb-run` and disabled the pytest Xvfb plugin; final command exited 0.
- `QT_QPA_PLATFORM=offscreen python3 -m pytest -q -p no:xvfb --tb=short --show-capture=no tests/unit/completion/test_models.py` failed at setup: `No display and no Xvfb available!`. Resolved by using `xvfb-run`.

No remaining verification uncertainty for the tested completion and config paths.
