# Checkpoint

Task: Resolve the pip module fallback when no pip executable is on PATH, using repository code and existing tests.

Completed: Added current-interpreter pip importability detection with `importlib.util.find_spec` and an `imp.find_module` compatibility fallback; `_get_pip` now falls back to `[sys.executable, '-m', 'pip']` and normalizes normal executable launchers to argv lists. Package listing uses argv, prefers `list --format=freeze`, falls back to `freeze`, and reports the final command as one string with stdout/stderr. Virtualenv PATH prefix is derived with `os.path.join(env, 'bin')`.

Verification: `pytest -q test/units/modules/test_pip.py` passed (4 tests).
