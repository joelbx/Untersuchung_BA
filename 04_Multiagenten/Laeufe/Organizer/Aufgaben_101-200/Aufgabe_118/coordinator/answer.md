Updated the pip module to use `sys.executable -m pip` when pip is available to the current interpreter. Launchers are now argv lists, package listing tries `list --format=freeze` before `freeze`, and virtualenv PATH setup uses `os.path.join`.

The focused pip tests pass: **9 passed**. `git diff --check` is clean. I solved this directly; no delegation or adoption was needed.