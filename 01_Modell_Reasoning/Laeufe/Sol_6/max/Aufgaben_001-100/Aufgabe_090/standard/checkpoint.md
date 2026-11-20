Task: Fix `/lists/add` input handling so POST form data takes precedence over query parameters, nested seeds parse safely, and duplicate simple assignments use the last value.

Progress: Updated `ListRecord.from_input` to parse POST bodies independently, apply safe defaults (including for nested query fields), and ignore invalid seed entries. Updated `utils.unflatten` so later simple assignments win and nested data can replace earlier scalar values. Added focused regression tests.

Verification: `pytest -q` on list, upstream utility, addbook, and forms test modules passed (34 tests). `ruff check` on changed Python files and `git diff --check` passed.
