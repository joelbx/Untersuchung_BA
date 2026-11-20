# Checkpoint

Task: fix pip module fallback when no pip executable is on PATH.
Status: complete.

Changes:
- Detect pip importability with importlib and a pkgutil fallback; treat detection errors as unavailable.
- Use the current interpreter with `-m pip` when appropriate, and represent every pip launcher as an argv list.
- Run package listing with argv, trying `list --format=freeze` before `freeze`; return a single quoted command string with stdout and stderr.
- Build the virtualenv path prefix with `os.path.join`.
- Add focused unit tests for launchers, listing fallback, module execution, detection error, and virtualenv path prefix.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/modules/test_pip.py` passed (12 tests). `git diff --check` passed.
