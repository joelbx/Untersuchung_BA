Updated the pip module to use the current Python interpreter’s `pip` package when available, even if no pip binary is on `PATH`. Launchers now use argv lists consistently; package listing tries `list` before falling back to `freeze`, and virtualenv paths use `os.path.join`.

Added regression tests for the reported case. All 9 pip unit tests pass.