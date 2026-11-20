# Checkpoint

Issue: make the pip module use the current interpreter's pip library when no pip executable is available.

Plan: inspect the module and existing tests, update pip discovery and package listing, then run relevant local tests.

Status: implemented and verified.

- `lib/ansible/modules/pip.py` now detects pip with `importlib.util.find_spec` and a `pkgutil.find_loader` fallback, invokes it through the current interpreter when appropriate, and keeps launchers as argv lists.
- Package listing tries `list --format=freeze` before `freeze` and returns the final command as a string. Virtualenv path prefixes use `os.path.join`.
- `test/units/modules/test_pip.py` covers missing binaries, module detection, listing fallback, explicit executables, and virtualenvs.
- Verification: `PYTHONPATH=lib python -m pytest -q test/units/modules/test_pip.py` (14 passed); `git diff --check` and `py_compile` passed.
