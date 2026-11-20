Updated [pip.py](/app/lib/ansible/modules/pip.py) to detect pip for the current interpreter, use `[sys.executable, '-m', 'pip']` when available, normalize launchers to argv lists, retain modern-to-legacy package listing fallback, and build the virtualenv PATH prefix with `os.path.join`.

Adjusted the existing pip-absent case in [test_pip.py](/app/test/units/modules/test_pip.py) to simulate pip being unavailable.

Validation passed: `PYTHONPATH=/app/lib python -m pytest test/units/modules/test_pip.py -q` (4 tests) and `git diff --check`.