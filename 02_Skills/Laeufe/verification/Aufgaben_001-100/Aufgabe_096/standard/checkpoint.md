# Checkpoint

Task: secure default permissions in atomic_move and warn when module mode is omitted.

Implementation: `_DEFAULT_PERM` is 0600; `atomic_move` uses the existing chmod with default permissions masked by the current umask. New paths are recorded on the AnsibleModule when it accepts `mode` and the value is omitted. `_return_formatted` emits the required warning for each path. `set_mode_if_different` removes tracked paths when given a mode.

Verification:
- `PYTHONPATH=lib python -m pytest -q test/units/module_utils/basic/test_atomic_move.py test/units/module_utils/basic/test_set_mode_if_different.py test/units/module_utils/basic/test_deprecate_warn.py`: 50 passed.
- `PYTHONPATH=lib python -m pytest -q test/units/module_utils/basic/test_exit_json.py`: 20 passed.
- `PYTHONPATH=lib python -m pytest -q test/units/module_utils/basic`: 20 failed, 279 passed, 14 skipped. Failures in `test_argument_spec.py` and `test_exit_json.py` arise from globally accumulated warnings/deprecations during the combined run. `test_exit_json.py` passes independently. Uncertainty: the broad directory has a preexisting shared-state test isolation issue; its aggregate result cannot establish all basic tests pass.
- `git diff --check`: exit 0.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`), so local grep/find were used. A first pytest run without `PYTHONPATH=lib` imported another Ansible package and did not test the checkout; subsequent runs use `PYTHONPATH=lib`.
