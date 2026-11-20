# Checkpoint

Investigating pip module launcher selection and package listing. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use `find`/`grep`.

## Investigation

`_get_pip` fails after PATH lookup without checking importability of pip for `sys.executable`. `main` assumes its return is a scalar (`[pip] + state_map[state]`); `_get_packages` interpolates it into a command string. This prevents a Python `-m pip` launcher and makes listing brittle. Virtualenv PATH prefix uses manual slash slicing. Existing working pattern: package operations pass argv lists to `module.run_command`.

Hypothesis: selecting `[sys.executable, '-m', 'pip']` when no explicit executable or virtualenv is set and pip is importable, with argv normalization and list-based listing execution, resolves the failure.

## Resolution and verification

Added a regression test before the fix. `PYTHONPATH=lib python -m pytest -q test/units/modules/test_pip.py -k test_get_pip_uses_current_interpreter_without_binary` failed as expected: `_get_pip` did not return `[sys.executable, '-m', 'pip']` when PATH lookup returned none. Two initial test setup runs failed because the existing fixture requires a mapping parameter; corrected the test parameter to `{}` before the expected failure.

The fix detects pip with `importlib.util.find_spec` and a `pkgutil.find_loader` fallback, returning false on detection errors. The default launcher uses the current interpreter when pip is available. All launcher results are argv lists. Package listing executes argv commands (`list --format=freeze`, then `freeze`) and returns the final command as one string with stdout and stderr. Virtualenv PATH prefix comes from `os.path.join(env, 'bin')`.

`PYTHONPATH=lib python -m pytest -q test/units/modules/test_pip.py`: 11 passed, exit 0. `git diff --check`: exit 0. No external checks or downloads used.
