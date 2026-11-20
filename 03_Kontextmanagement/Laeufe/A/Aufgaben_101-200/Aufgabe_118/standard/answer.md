Fixed the pip module so it uses the current interpreter’s `python -m pip` when pip is importable and no executable or virtualenv is specified. Package listing now tries `list` before falling back to `freeze`, and virtualenv path handling uses `os.path.join`.

The relevant unit tests pass: **9 passed**.