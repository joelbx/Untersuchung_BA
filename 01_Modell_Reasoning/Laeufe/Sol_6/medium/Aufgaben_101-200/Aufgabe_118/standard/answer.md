Updated the pip module to use `sys.executable -m pip` when pip is available to the current interpreter. Launcher commands now use argv lists, package listing tries `list --format=freeze` before `freeze`, and virtualenv path construction uses `os.path.join`.

The pip unit tests pass: **9 passed**. `git diff --check` also passed.