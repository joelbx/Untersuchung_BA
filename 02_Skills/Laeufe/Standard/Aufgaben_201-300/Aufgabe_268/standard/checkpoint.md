# Checkpoint

Task: Include command and error type in GUI process startup errors, with a Unix executable hint for missing or denied commands.

Status: Implementation and tests updated. `rg` is unavailable; used local grep/find instead.

Changed: `_on_error` now includes the capitalized process name, quoted command, code-specific wording, and process error detail. Missing or non-executable commands receive the required hint on non-Windows systems. Detached startup failures use the same handler. Updated unit and BDD expectations.

Checks:
- `xvfb-run -a python -m pytest -p no:xvfb -q -o addopts= tests/unit/misc/test_guiprocess.py`: 32 passed, exit 0.
- `git diff --check`: passed.
- `xvfb-run -a python -m pytest -p no:xvfb -q -o addopts= tests/end2end/features/test_spawn_bdd.py -k 'command_that_does_not_exist'`: failed before the scenario ran because the QtWebKit backend could not import `QtWebKit` from `PyQt5`. The BDD message expectation remains unverified in this environment.
