# Checkpoint

Issue: Update the Ansible pip module to use the current interpreter's pip library when no executable or virtualenv is specified, preserve listing fallback/logging behavior, and derive virtualenv executable paths with OS path joins.

Implemented in `lib/ansible/modules/pip.py`: `_have_pip_module()` detects pip with `importlib.util.find_spec` and falls back to `imp.find_module` on older interpreters; `_get_pip()` returns argv lists and selects `[sys.executable, '-m', 'pip']` when applicable; package listing runs modern `list --format=freeze` and falls back to `freeze`, with a quoted command string for logging; virtualenv PATH prefix uses `os.path.join(env, 'bin')`.

Updated the existing pip-absent unit case to explicitly model an interpreter without the pip library.

Validation: `PYTHONPATH=/app/lib python -m pytest test/units/modules/test_pip.py -q` passed (4 tests); `git diff --check` passed. The plain pytest invocation initially resolved the globally installed Ansible package, so validation used the checkout's `lib` directory on `PYTHONPATH`.
