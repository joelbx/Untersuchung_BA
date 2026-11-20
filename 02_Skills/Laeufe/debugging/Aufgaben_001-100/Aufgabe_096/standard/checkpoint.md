# Checkpoint

Task: resolve insecure default permissions and warning tracking for `atomic_move()`.

Status: root cause reproduced; implementing fix. `rg` is unavailable in the environment; using local `grep`/`find` instead.

Evidence: `atomic_move()` already chmods new destinations with `DEFAULT_PERM & ~umask`, but `_DEFAULT_PERM` is `0666`, so umask `022` yields `0644`. There is no created-path tracking or warning hook. New regression tests failed with actual chmod mode 420 (`0644`) versus 384 (`0600`), and missing `_created_files`.

Hypothesis confirmed: changing `_DEFAULT_PERM` to `0600`, recording newly created paths when `mode` is available and omitted, and clearing those paths on an explicit mode call satisfies the requested behavior. Existing destination permissions remain preserved.

Verification:
- `PYTHONPATH=lib python -m pytest -q --reruns 0 test/units/module_utils/basic/test_atomic_move.py test/units/module_utils/basic/test_set_mode_if_different.py test/units/module_utils/basic/test_exit_json.py`: 66 passed.
- `PYTHONPATH=lib python -m pytest -q --reruns 0 --forked test/units/module_utils/basic test/units/module_utils/common`: 1053 passed, 14 skipped.
- `git diff --check`: passed.

The same broad suite without `--forked` had 33 failures because existing tests share process-global warning/deprecation lists across cases; isolated execution passes. An initial test command omitted `PYTHONPATH=lib` and imported an installed Ansible copy, so it was rerun against repository code. A broader command also initially named a nonexistent `test_file.py`; it was rerun with the correct directory paths.

Constraints: no network, no dependency downloads, no git history/index/harness changes.
