Updated the pip module to use the current Python interpreter’s pip package when no executable or virtualenv is specified. Package listing now tries `list --format=freeze` before `freeze`, and virtualenv path handling uses `os.path.join`.

The pip unit suite passes: **9 tests passed**.