# List model typing checkpoint

- Task: type List and Seed public APIs, normalize and validate seed keys, and update related helpers.
- Completed: added SeedDict and SeedSubjectString typing, typed List/Seed public methods, normalized seed key comparisons, subject conversion and guard helpers, and loaded/type-filtered exports. Added focused tests and return types for URL helpers.
- Verification: 21 relevant pytest tests passed; focused mypy and Ruff checks passed; git diff --check passed.
- Note: the separate legacy test_listapi.py cannot collect in this environment because its cookielib import is unavailable on Python 3.
