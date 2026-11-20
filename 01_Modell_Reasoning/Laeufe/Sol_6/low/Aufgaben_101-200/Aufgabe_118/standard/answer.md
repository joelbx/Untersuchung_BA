Updated the pip module to use the current interpreter’s pip package when no executable or virtualenv is specified. Launchers are now argv lists, package listing tries `list --format=freeze` before `freeze`, and virtualenv path prefixes use `os.path.join`.

Added focused tests. `PYTHONPATH=lib python -m pytest -q test/units/modules/test_pip.py` passed: 6 tests.